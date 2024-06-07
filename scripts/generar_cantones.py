from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Canton, Provincia
from configuration import string_connection

engine = create_engine(string_connection)

Session = sessionmaker(bind= engine)
session = Session()


file = open('data/instituciones.csv', mode='r')
data = file.readlines()
data = [line.split('|') for line in data]
data = data[1:]
data = list({(int(line[4]), line[5], int(line[2])) for line in data})
for line in data:
    provincia = session.query(Provincia).filter(Provincia.id == line[2]).one()
    canton = Canton(id = int(line[0]), canton=line[1], provincia = provincia)
    print(canton)
    session.add(canton)

session.commit()