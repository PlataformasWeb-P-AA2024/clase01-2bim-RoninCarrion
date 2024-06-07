from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Provincia
from configuration import string_connection

engine = create_engine(string_connection)

Session = sessionmaker(bind= engine)
session = Session()


file = open('data/instituciones.csv', mode='r')
data = file.readlines()
data = [line.split('|') for line in data]
data = data[1:]
data = list({(int(line[2]), line[3]) for line in data})

for line in data:
    provincia = Provincia(id = int(line[0]), provincia=line[1]) # Pos 0 código provincia
    print(provincia)
    session.add(provincia)

session.commit()