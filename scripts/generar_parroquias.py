from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Provincia, Canton, Parroquia
from configuration import string_connection

engine = create_engine(string_connection)
Session = sessionmaker(bind= engine)
session = Session()

file = open('data/data.csv', mode = 'r')
lines = file.readlines()
lines = [line.split('|') for line in lines]
lines = lines[1:]
lines = list({(str(line[6]), line[7], int(line[4])) for line in lines})

print(lines)
for data in lines:
    canton = session.query(Canton).filter(Canton.id == data[2]).one()
    parroquia = Parroquia(id=data[0], name = data[1], canton=canton)
    print(parroquia)
    session.add(parroquia)
session.commit()
