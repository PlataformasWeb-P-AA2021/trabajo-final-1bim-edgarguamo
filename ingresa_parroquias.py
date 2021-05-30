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

parroquia_data = df.iloc[:,[6,7,4]]
parroquia_data = parroquia_data.drop_duplicates().sort_values('codigo_parroquia')

parroquias = parroquia_data.values.tolist()

for p in parroquias:
    registro_parroquias = Parroquia(id = p[0], nombre = p[1],
            canton = session.query(Canton).filter_by(id= p[2]).one())
    session.add(registro_parroquias)
session.commit()
