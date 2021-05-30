from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importación de la clase con las tablas
from genera_tablas import Provincia
# Libreria para leer csv
import pandas as pd

from estructurar_datos import df

engine = create_engine("sqlite:///instituciones.db")

Session = sessionmaker(bind=engine)
session = Session()

# print(df.head())

provincia_data = df.iloc[:,[2,3]]
provincia_data = provincia_data.drop_duplicates().sort_values('codigo_provincia')
# print(provincia_data.head())
provincias = provincia_data.values.tolist()

for p in provincias:
    registro_provincia = Provincia(id = p[0], nombre = p[1])
    session.add(registro_provincia)

session.commit()
