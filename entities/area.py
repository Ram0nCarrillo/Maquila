from sqlalchemy import Column, Integer, String, TEXT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Area(Base):
    __tablename__ = 'area'
    id = Column(Integer, primary_key = True)
    departamento = Column(String, nullable=False)
    descripcion = Column(TEXT)
    
from sqlalchemy.orm import relationship
supervisores = relationship("Supervisor", back_populates="area")
operadores = relationship("Operador", back_populates="area")