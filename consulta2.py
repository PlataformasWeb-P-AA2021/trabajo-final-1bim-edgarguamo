# Librerias necesarias para usar sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, distinct # se importa el operador and

# Importación de las tablas
from genera_tablas import Provincia, Canton, Parroquia, Instituto

# Establecimiento del db a usar
engine = create_engine('sqlite:///instituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 2.1 Las parroquias que tienen establecimientos únicamente enla jornada
# nocturna

instituciones_nocturnos = session.query(Parroquia.nombre,Instituto.parroquia_id,
        Parroquia.id).distinct(Parroquia.nombre)\
                .join(Instituto).filter(Instituto.jornada.\
                like('Nocturna')).all()
print('\n-------------------------- \n Consulta 2.1 \n -----------------------\n')
for insti in instituciones_nocturnos:
    print(insti[0])

#Consulta 2.2 Los cantones que tiene establecimientos como número de estudiantes tales como:
# 448,450,451,454,458,459

instituciones_cantones = session.query(Canton.nombre,
        Instituto.parroquia_id,Parroquia.id,
        Parroquia.id_cantones,Canton.id).distinct(Canton.nombre)\
        .join(Instituto,Canton).filter(or_(Instituto.num_estudiantes== 448,
            Instituto.num_estudiantes==450,Instituto.num_estudiantes==451,
            Instituto.num_estudiantes==454, Instituto.num_estudiantes==458,
            Instituto.num_estudiantes==459)).all()
print('\n -------------------- \n Consulta 2.2 \n ----------------------- \n')
aux = []
for insti in instituciones_cantones:
    aux.append(insti[0])

conjunto = set(aux)
for dato in conjunto:
    print(dato)
