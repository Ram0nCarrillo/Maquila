from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Area(Base):
    __tablename__ = 'area'
    id = Column(Integer, primary_key = True)
    corte = Column(String)
    ensamble = Column(String)
    empaque = Column(String)
    acabado = Column(String)
    # Relaciones
    supervisores = relationship("Supervisor", back_populates="area")
    operadores = relationship("Operador", back_populates="area")