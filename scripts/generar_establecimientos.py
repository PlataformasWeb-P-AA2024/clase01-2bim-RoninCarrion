from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Parroquia, Establecimiento
from configuration import string_connection

engine = create_engine(string_connection)
Session = sessionmaker(bind= engine)
session = Session()

establecimientosList = []
file = open('data/instituciones.csv', mode = 'r')
lines = file.readlines()
lines = [line.split('|') for line in lines]
lines = lines[1:]
lines = list({(
            line[0], # código amie
            line[1], # nombre institución
            line[6], # codigo parroquia
            #line[7], # nombre parroquia
            line[8], # zona
            line[9], # nombre distrito
            line[10], # codigo distrito
            line[11], # codigo circuito
            line[12], # sostenimiento
            line[13], # regimen escolar
            line[14], # jurisdicción
            line[15], #tipo educación
            line[16], # modalidad
            line[17], # jornada
            line[18], # nivel
            line[19], # etnia, 
            line[20], # acceso 
            line[21], # número estudiantes
            line[22], # número docentes
            line[23] # estado
            
            ) for line in lines})

print(lines)
for data in lines:
    parroquia = session.query(Parroquia).filter(Parroquia.id == data[2]).one()
    establecimiento = Establecimiento(
    codigo_amie = data[0],
    nombre =  data[1],
    parroquia_id =  data[2],
    parroquia =  parroquia,
    zona =  data[3],
    nombre_distrito =  data[4],
    codigo_distrito =  data[5],
    codigo_circuito =  data[6],
    sostenimiento =  data[7],
    regimen_escolar =  data[8],
    jurisdiccion =  data[9],
    tipo_educacion =  data[10],
    modalidad =  data[11],
    jornada =  data[12],
    nivel =  data[13],
    etnia =  data[14],
    acceso =  data[15],
    numero_estudiantes = int(data[16]),
    numero_docentes = int(data[17]),
    estado = data[18],
        )
    print(establecimiento)
    session.add(establecimiento)
session.commit()
