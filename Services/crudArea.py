from entities.area import Area
from persistence.db import SessionLocal

session = SessionLocal()

def get():
    clientes = SessionLocal().query(Area).all()
    for a in clientes:
        print(f"\nId: {a.id}\Corte: {a.corte}\nEnsamble: {a.ensamble}\nEmpaque: {a.empaque}\nAcabado: {a.acabado}")
def get():
    areas = SessionLocal().query(Area).all()
    for a in areas:
        print(f"\nId: {a.id}")
        print(f"\Departamento: {a.departamento}")
        print(f"\nDescripcion: {a.descripcion}")