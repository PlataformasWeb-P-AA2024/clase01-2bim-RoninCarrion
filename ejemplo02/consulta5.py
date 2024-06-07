from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

# se importa la clase(s) del 
# archivo genera_tablas
from generar_tablas import Provincia, Parroquia, Canton, Establecimiento

# se importa información del archivo configuracion
from configuration import string_connection

engine = create_engine(string_connection)

Session = sessionmaker(bind=engine)
session = Session()


# Todos los establecimientos que pertenecen al Código División Política
# Administrativa Parroquia con valor 020151 y 020153

data = session.query(Provincia).all()

for provincia in data:
    print(f"""> Provincia: {provincia.provincia}
> Lista Parroquias:\n {provincia.obtenerListaParroquias()}""")
    

    
