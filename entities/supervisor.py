from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Supervisor(Base):
    __tablename__ = 'supervisor'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    telefono = Column(String)
    correo = Column(String)
    turno = Column(String)
    
from sqlalchemy.orm import relationship
id_area = Column(Integer, ForeignKey("area.id"))
area = relationship("Area", back_populates="supervisores")
# Relaciones
operadores = relationship("Operador", back_populates="supervisor")