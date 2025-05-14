from entities.supervisor import Supervisor
from persistence.db import SessionLocal

session = SessionLocal()

def get():
    supervisores = SessionLocal().query(Supervisor).all()
    for s in supervisores:
        print(f"\nId: {s.id}")
        print(f"\nNombre: {s.nombre}")
        print(f"\nTelefono: {s.telefono}")
        print(f"\nCorreo: {s.correo}")
        print(f"\nTurno: {s.turno}")
        print(f"\nÁrea: {s.area if s.area else 'No asignada'}")
        

        
def save(nombre, telefono, correo, turno, id_area):
    SessionLocal().query(Supervisor).all()
    s = Supervisor(nombre = nombre, telefono = telefono, correo = correo, turno = turno, id_area = id_area)
    session.add(s)
    session.commit()
    print(f"\nSe agrego al registro a {s.nombre}")
 
def update(id, nombre, telefono, correo, turno, id_area):
    supervisor = session.query(Supervisor).filter_by(id = id).first()
    if supervisor:
        supervisor.nombre = nombre
        supervisor.telefono = telefono
        supervisor.correo = correo
        supervisor.turno = turno
        supervisor.id_area = id_area
        session.commit()
        print("Guardado exitoso")
    else:
        print("El supervisor ingresado no existe")
 
def delete(id):
    cliente = session.query(Supervisor).filter_by(id = id).first()
    if cliente:
        session.delete(cliente)
        session.commit
    else:
        print("El supervisor ingresado no existe")