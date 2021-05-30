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

instituto_data = df.iloc[:,[0,1,8,9,10,11,12,13,14,15,6]]

instituto = instituto_data.values.tolist()

for i in instituto:
    registro_instituto = Instituto(id = i[0],nombre = i[1], codigo_DPA = i[2],
            sostenimiento = i[3], tipo_eduación = i[4], modalidad = i[5], jornada = i[6],
            acceso = i[7], num_estudiantes = i[8], num_docentes = i[9],
            parroquia = session.query(Parroquia).filter_by(id=i[10]).one())
    session.add(registro_instituto)

session.commit()
