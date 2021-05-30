from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column,Float, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///instituciones.db')
Base = declarative_base()

"""
Este modulo tiene como objetivo crear las tablas de la base de datos
"""
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    cantones = relationship('Canton', back_populates = 'provincia')
    def __repr__(self):
        return '\n Provincia = %.0f \n nombbre Provincia = %s' % (self.id, self.nombre)

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    id_provincia =  Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship('Provincia', back_populates = 'cantones')
    parroquias = relationship('Parroquia', back_populates = 'canton')
    def __repr__(self):
        return '\n Canton_id = %.0f \n Nombrec Canton= %s \n id_provincia = %s \n' %(
                self.id,
                self.nombre,
                self.id_provincia
                )

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    id_cantones = Column(Integer, ForeignKey('canton.id'))
    canton = relationship('Canton', back_populates = 'parroquias')
    institutos = relationship('Instituto', back_populates='parroquia')

class Instituto(Base):
    __tablename__ = 'instituto'
    id = Column(String, primary_key=True)
    nombre = Column(String)
    codigo_DPA = Column(String)
    sostenimiento = Column(String)
    tipo_eduación = Column(String)
    modalidad = Column(String)
    jornada = Column(String)
    acceso = Column(String)
    num_estudiantes = Column(Integer)
    num_Docentes = Column(Integer)
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    parroquia = relationship('Parroquia', back_populates='institutos')
    def __repr__(self):
        return '\n Instituto_id = %s \n nombre Instituto= %s \n codigo_DPA = %s \n '\
                'Sostenimiento = %s \n tipo de educación = %s \n modalidad =%s \n '\
                'Jornada = %s \n Acceso = %s \n Número de estudiantes = %s \n '\
                'Número de Doccentes = %s \n' % (
                        self.id,
                        self.nombre,
                        self.codigo_DPA,
                        self.sostenimiento,
                        self.tipo_eduación,
                        self.modalidad,
                        self.jornada,
                        self.acceso,
                        self.num_estudiantes,
                        self.num_Docentes
                )

Base.metadata.create_all(engine)

