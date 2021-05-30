from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importación de la clase con las tablas
from genera_tablas import Provincia, Canton, Parroquia, Instituto
# Libreria para leer csv
import pandas as pd
from estructurar_datos import df
engine = create_engine("sqlite:///instituciones.db")

Session = sessionmaker(bind=engine)
session = Session()

cantones_data = df.iloc[:,[4,5,2]]
cantones_data = cantones_data.drop_duplicates().sort_values('codigo_canton')

cantones = cantones_data.values.tolist()
for c in cantones:
    registro_cantones = Canton(id=c[0], nombre = c[1],
            provincia = session.query(Provincia).filter_by(id = c[2]).one())
    session.add(registro_cantones)

session.commit()
