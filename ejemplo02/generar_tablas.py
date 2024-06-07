from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# Se importa información del archivo configuración
from configuration import string_connection

# Crear el motor de la base de datos
engine = create_engine(string_connection)

# Base para las clases
Base = declarative_base()

# Definición de la tabla Provincia
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    provincia = Column(String(100))  # Especificar longitud

    def __repr__(self):
        return f"<Provincia(id={self.id}, provincia='{self.provincia}')>"

    # A cada provincia perdile el número de docentes
    def obtenerNumeroDocentes(self):
        
        

        listaEstablecimientos = [canton.obtenerNumeroDocentes() for canton in self.cantones]

        suma = sum(listaEstablecimientos)
        return suma
    
    # A cada provincia preguntar la lista de parroquias

    def obtenerListaParroquias(self):
        cadena = ""
        listaParroquias = [canton.parroquias for canton in self.cantones]

        for parroquiasCantones in listaParroquias:
            for parroquia in parroquiasCantones:
                cadena += f"> {parroquia.name}\n"
        return cadena





# Definición de la tabla Cantón
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    canton = Column(String(100))  # Especificar longitud
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship('Provincia', back_populates='cantones')

    def __repr__(self):
        return f"<Canton(id={self.id}, canton='{self.canton}', provincia_id={self.provincia_id})>"


    # A cada cantón pedirle el número de estudiantes

    def obtenerNumeroEstudiantes(self):
    
        listaEstablecimientos = [parroquia.establecimientos for parroquia in self.parroquias]

        suma = 0
        for establecimientoParroquia in listaEstablecimientos:
            for establecimiento in establecimientoParroquia:
                suma += establecimiento.numero_estudiantes
        return suma
    
    def obtenerNumeroDocentes(self):
    
        listaEstablecimientos = [parroquia.establecimientos for parroquia in self.parroquias]

        suma = 0
        for establecimientoParroquia in listaEstablecimientos:
            for establecimiento in establecimientoParroquia:
                suma += establecimiento.numero_docentes


        #listaNumEstudiantes = [establecimiento.numero_estudiantes for establecimiento in (establecimientoParroquias for establecimientoParroquias in listaEstablecimientos)]
        return suma
         
    








# Definición de la tabla Parroquia
class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(String(50), primary_key=True)
    name = Column(String(100))  # Especificar longitud
    canton_id = Column(Integer, ForeignKey('canton.id'))
    canton = relationship('Canton', back_populates='parroquias')

    def __repr__(self):
        return f"<Parroquia(id={self.id}, name='{self.name}', canton_id={self.canton_id})>"
    
    # A cada parroaquia preguntar el número de establecimientos

    def obtenerNumeroEstablecimientos(self):
        return len(self.establecimientos)
    
    def obtenerJornadas(self):
        tiposJornadas = []
        cadena = ""
        for establecimiento in self.establecimientos:
            tiposJornadas.append(establecimiento.jornada)

        for jornada in set(tiposJornadas):
            cadena += f"{jornada}  "
        return cadena









# Definición de la tabla Establecimiento
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigo_amie = Column(String(20))  # Especificar longitud
    nombre = Column(String(100))  # Especificar longitud
    parroquia_id = Column(String(50), ForeignKey('parroquia.id'))
    parroquia = relationship('Parroquia', back_populates='establecimientos')
    zona = Column(String(50))  # Especificar longitud
    nombre_distrito = Column(String(100))  # Especificar longitud
    codigo_distrito = Column(String(50))  # Especificar longitud
    codigo_circuito = Column(String(50))  # Especificar longitud
    sostenimiento = Column(String(50))  # Especificar longitud
    regimen_escolar = Column(String(50))  # Especificar longitud
    jurisdiccion = Column(String(50))  # Especificar longitud
    tipo_educacion = Column(String(50))  # Especificar longitud
    modalidad = Column(String(50))  # Especificar longitud
    jornada = Column(String(50))  # Especificar longitud
    nivel = Column(String(50))  # Especificar longitud
    etnia = Column(String(50))  # Especificar longitud
    acceso = Column(String(50))  # Especificar longitud
    numero_estudiantes = Column(Integer)
    numero_docentes = Column(Integer)
    estado = Column(String(50))  # Especificar longitud

    def __repr__(self):
        return (f"<Establecimiento(id={self.id}, codigo_amie='{self.codigo_amie}', nombre='{self.nombre}', "
                f"parroquia_id={self.parroquia_id}, zona='{self.zona}', nombre_distrito='{self.nombre_distrito}', "
                f"codigo_distrito='{self.codigo_distrito}', codigo_circuito='{self.codigo_circuito}', "
                f"sostenimiento='{self.sostenimiento}', regimen_escolar='{self.regimen_escolar}', "
                f"jurisdiccion='{self.jurisdiccion}', tipo_educacion='{self.tipo_educacion}', "
                f"modalidad='{self.modalidad}', jornada='{self.jornada}', nivel='{self.nivel}', "
                f"etnia='{self.etnia}', acceso='{self.acceso}', numero_estudiantes={self.numero_estudiantes}, "
                f"numero_docentes={self.numero_docentes}, estado='{self.estado}')>")


Provincia.cantones = relationship('Canton', order_by=Canton.id, back_populates='provincia')
Canton.parroquias = relationship('Parroquia', order_by=Parroquia.id, back_populates='canton')
Parroquia.establecimientos = relationship('Establecimiento', order_by=Establecimiento.id, back_populates='parroquia')

Base.metadata.create_all(engine)
