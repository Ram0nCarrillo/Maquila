from entities.operador import Operador
from persistence.db import SessionLocal

session = SessionLocal()

def get():
    operadores = SessionLocal().query(Operador).all()
    for o in operadores:
        print(f"\nId: {o.id}")
        print(f"\nNombre: {o.nombre}")
        print(f"\Sexo: {o.sexo}")
        print(f"\Fecha Ingresada: {o.fecha_ingreso}")
        print(f"\Turno: {o.turno}")
        print(f"\Salario: {o.salario}")
        print(f"\nÁrea: {o.area if o.area else 'No asignado'}")
        print(f"\Supervisor: {o.supervisor if o.supervisor else 'No asignado'}")

        
def save(nombre, sexo, fecha_ingreso, turno, salario, id_area, id_supervisor):
    SessionLocal().query(Operador).all()
    o = Operador(nombre = nombre, sexo = sexo, fecha_ingreso = fecha_ingreso, turno = turno, 
                 salario = salario, id_area = id_area, id_supervisor = id_supervisor)
    session.add(o)
    session.commit()
    print(f"\nSe agrego al registro a {o.nombre}")
 
def update(id, nombre, sexo, fecha_ingreso, turno, salario, id_area, id_supervisor):
    operador = session.query(Operador).filter_by(id = id).first()
    if operador:
        operador.nombre = nombre
        operador.sexo = sexo
        operador.fecha_ingreso = fecha_ingreso
        operador.turno = turno
        operador.salario = salario
        operador.id_area = id_area
        operador.id_supervisor = id_supervisor
        operador.commit()
        print("Guardado exitoso")
    else:
        print("Fallo")
 
def delete(id):
    cliente = session.query(Operador).filter_by(id = id).first()
    if cliente:
        session.delete(cliente)
        session.commit
    else:
        print("El operador ingresado no existe")