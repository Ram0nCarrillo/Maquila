from sqlalchemy import Column, Integer, String, DECIMAL, Date, CHAR, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Operador(Base):
    __tablename__ = 'operador'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    sexo = Column(CHAR)
    fecha_ingreso = Column(Date)
    turno = Column(String)
    salario = Column(DECIMAL)

from sqlalchemy.orm import relationship
id_supervisor = Column(Integer, ForeignKey("supervisor.id"))
supervisores = relationship("Supervisor", back_populates="operadores")
id_area = Column(Integer, ForeignKey("area.id"))
area = relationship("Area", back_populates="operadores")    