from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, distinct # se importa el operador and

# Importación de tablas a usar
from genera_tablas import Provincia, Canton, Parroquia, Instituto

engine = create_engine('sqlite:///instituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

"""
Consulta 3.1 Los cantones que tiene establecimientos con 0 número de profesores
"""
"""
Para esta consulta es necesario emplear la función distinct, pero sqlAchemy
solo permite esta opción si se usa postgres, por lo que es necesario un filtrado
externo
"""

profesores_cantones = session.query(Canton.nombre, Instituto.parroquia_id,
        Parroquia.id,Parroquia.id_cantones, Canton.id).distinct(Canton.nombre)\
        .join(Instituto, Canton).filter(Instituto.num_Docentes==0).all()


print('\n -------------------- \n Consulta 1.2 \n ----------------------- \n')

"""
El filtrado externo trata del almacenamiento del nombre de los cantones en un
conjunto y luego presentarlo al usuario
"""

aux = []
for prof in profesores_cantones:
    aux.append(prof[0])

conjunto = set(aux)
for dato in conjunto:
    print(dato)
"""
Consulta 3.2 Los establecimientos que pertenecen a la parroquia Catacocha con
estudiantes mayores o iguales a 21
"""
"""
Se presenta el mismo problema, pero con la peculariedad de que los nombres
de instituciones no se repite, por lo que el distinct no es  necesario
"""

est_catacocha = session.query(Instituto.nombre,Instituto.parroquia_id,Parroquia)\
        .join(Instituto).filter(and_(Parroquia.nombre.like('Catacocha'),
            Instituto.num_estudiantes >=21)).all()

print('\n -------------------- \n Consulta 3.2 \n ----------------------- \n')
for est in est_catacocha:
    print(est[0])


