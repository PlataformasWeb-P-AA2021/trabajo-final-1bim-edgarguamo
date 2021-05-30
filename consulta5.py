from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, distinct # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Parroquia, Instituto

engine = create_engine('sqlite:///instituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

"""
Consulta 5.1: Los establecimientos ordenados por nombre de parroquia que tengan
más de 20 profesores y la cadena 'permanente' en tipo de educación
"""

consulta51 = session.query(Instituto, Parroquia).join(Instituto)\
        .filter(and_(Instituto.tipo_eduación.like('%permanente%')),
                Instituto.num_Docentes >20).order_by(Parroquia.nombre).all()

print('\n -------------------- \n Consulta 5.1 \n ----------------------- \n')
for c in consulta51:
    print(c)

"""
Consulta 5.2: Todos los establecimientos ordenados por sostenimiento
y tengan codigo_DPA 11D02
"""

consulta52 = session.query(Instituto).filter(Instituto.codigo_DPA.like('11D02'))\
        .order_by(Instituto.sostenimiento).all()

print('\n -------------------- \n Consulta 5.2 \n ----------------------- \n')
for c in consulta52:
    print(c)
