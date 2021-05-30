from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, distinct # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Parroquia, Instituto

engine = create_engine('sqlite:///instituciones.db')
Session = sessionmaker(bind=engine)
session = Session()


print('\n -------------------- \n Consulta 1.2 \n ----------------------- \n')
"""
Consulta 4.1 Los establecimientos ordenados por número de estudiantes; que
tengan más de 100 profesores
"""
"""
Consulta a tabla unitaria
"""

consulta41 = session.query(Instituto).filter(Instituto.num_Docentes >= 100)\
        .order_by(Instituto.num_estudiantes)

print('\n -------------------- \n Consulta 4.2 \n ----------------------- \n')

for c in consulta41:
    print(c)
"""
Consulta 4.2 Los establecimientos ordenados por número de profesores: que
tengan más de 100 profesores
"""
"""
Consulta Unitaria
"""
consulta42 = session.query(Instituto).filter(Instituto.num_Docentes>=100)\
        .order_by(Instituto.num_Docentes)

print('\n -------------------- \n Consulta 1.2 \n ----------------------- \n')
for c in consulta42:
    print(c)

