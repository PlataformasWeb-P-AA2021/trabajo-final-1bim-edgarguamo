import pandas as pd
"""
Este modulo tiene como objetivo leer la información del archivo csv y formar un
dataframe con este, además de cambiar el nombre de las columnas a unas más simples
"""
csv_file = './data/Listado-Instituciones-Educativas.csv'

#l lectura del archivo csv
df = pd.read_csv(csv_file, sep='|')

#Cambio de nombre a las columnas
df.columns = ['codigo_instituto','nombre_instituto', 'codigo_provincia',
        'provincia','codigo_canton', 'canton', 'codigo_parroquia', 'parroquia',
        'codigo_distrito', 'sostenimiento', 'tipo_educacion','modalidad',
        'jornada', 'acceso','numero_estudiantes','numero_docentes']


