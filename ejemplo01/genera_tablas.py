from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
import datetime

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Ejemplo que representa la relación entre dos clases
# One to Many
# Un club tiene muchos jugadores asociados

class Club(Base):
    __tablename__ = 'club'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    deporte = Column(String(100))
    fundacion = Column(Integer, nullable=False)
    # Mapea la relación entre las clases
    # Club puede acceder a los jugadores asociados
    # por la llave foránea
    jugadores = relationship("Jugador", back_populates="club")



    def obtenerAniosVida(self):
        return datetime.datetime.now().year - self.fundacion
    


    def obtenerDorsales(self):
        cadena = ""
        for dorsal in [dorsal.dorsal for dorsal in self.jugadores]:
            cadena += f"{dorsal}  "
        return cadena
    
    def obtenerSumaDorsales(self):
        # sumaDorsales = 0                                                  
        # for dorsal in [dorsal.dorsal for dorsal in self.jugadores]:
        #     sumaDorsales += dorsal
        # return sumaDorsales

        return sum([jugador.dorsal for jugador in self.jugadores]) #Ejemplo de lists comprehension en python, en donde estamos recorriendo cada uno de los jugadores,
                                                                # Extrayendo su dorsal y asignandolo a una lista para a este aplicarle la función sum y poder sumar cada
                                                                # uno de los dorsales que se encuentran dentro.
        
    

    
    def __repr__(self):
        return "Club: nombre=%s deporte=%s fundación=%d" % (
                          self.nombre, 
                          self.deporte, 
                          self.fundacion)

class Jugador(Base):
    __tablename__ = 'jugador'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    dorsal = Column(Integer)
    posicion = Column(String(100))
    # se agrega la columna club_id como ForeignKey
    # se hace referencia al id de la entidad club
    club_id = Column(Integer, ForeignKey('club.id'))
    # Mapea la relación entre las clases
    # Jugador tiene una relación con Club
    club  = relationship("Club", back_populates="jugadores")
    
    def __repr__(self):
        return "Jugador: %s - dorsal:%d - posición: %s" % (
                self.nombre, self.dorsal, self.posicion)
    
    


Base.metadata.create_all(engine)









