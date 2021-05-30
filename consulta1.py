from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# Importación de las tablas
from genera_tablas import Provincia, Canton, Parroquia, Instituto

engine = create_engine('sqlite:///instituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1.1 Todos los establecimientos de la prvincia de Loja

"""
Es necesario acceder a provincia desde instituto por lo que se debe hacer
una consulta multi-tablas
"""
insti_prov_loja= session.query(Provincia, Canton, Parroquia, Instituto)\
        .join(Instituto,Canton,Provincia).filter(Provincia.nombre.like('Loja'))\
        .all()
#Construcción del mensaje de salida
for insti in insti_prov_loja:
    print(' Provincia: %d \n Nombre Provincia: %s \n Codigo Canton: %0.f \n '\
            'Nombre Canton: %s \n Nombre Instituto: %s \n'\
            '-------------------------------'
            % (insti[0].id, insti[0].nombre, insti[1].id, insti[1].nombre,
                insti[3].nombre))

#Consulta 1.2 Todos los establecimientos del canton Loja

"""
Presenta la misma lógica que la primera consulta solo que no vincula a la tabla
provincia
"""
insti_canton_loja = session.query(Canton, Parroquia, Instituto)\
        .join(Instituto,Canton).filter(Canton.nombre.like('Loja')).all()

for insti in insti_canton_loja:
    print(' \n Codigo Canton: %0.f \n '\
            'Nombre Canton: %s \n Nombre Instituto: %s \n'\
            '-------------------------------'
            % (insti[0].id, insti[0].nombre, insti[2].nombre))


"""
Verificación: Consulta para saber el num de instituciones
"""
num_insti_prov_loja= session.query(Provincia, Canton, Parroquia, Instituto)\
        .join(Instituto,Canton,Provincia).filter(Provincia.nombre.like('Loja'))\
        .count()
print('Numero notal de Institutos en la provincia de Loja: %d' % num_insti_prov_loja)

num_insti_prov_loja= session.query(Canton, Parroquia, Instituto)\
        .join(Instituto,Canton).filter(Canton.nombre.like('Loja')).count()
print('Numero notal de Institutos en el canton de Loja: %d' % num_insti_prov_loja)


