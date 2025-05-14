import tkinter as tk
from tkinter import ttk
from Services.crudArea import get as get_areas
from Services.crudSupervisor import get as get_supervisores
from Services.crudOperador import get as get_operadores

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Maquila")
root.geometry("800x600")

# Crear las pestañas
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Pestaña de Áreas
frame_area = ttk.Frame(notebook)
notebook.add(frame_area, text='Áreas')

tree_area = ttk.Treeview(frame_area, columns=("ID", "Departamento", "Descripcion"), show='headings')
for col in tree_area["columns"]:
    tree_area.heading(col, text=col)
tree_area.pack(fill='both', expand=True)

# Pestaña de Supervisores
frame_supervisor = ttk.Frame(notebook)
notebook.add(frame_supervisor, text='Supervisores')

tree_supervisor = ttk.Treeview(frame_supervisor, columns=("ID", "Nombre", "Teléfono", "Correo", "Turno", "Área"), show='headings')
for col in tree_supervisor["columns"]:
    tree_supervisor.heading(col, text=col)
tree_supervisor.pack(fill='both', expand=True)

# Pestaña de Operadores
frame_operador = ttk.Frame(notebook)
notebook.add(frame_operador, text='Operadores')

tree_operador = ttk.Treeview(frame_operador, columns=("ID", "Nombre", "Sexo", "Fecha Ingreso", "Turno", "Salario", "Área", "Supervisor"), show='headings')
for col in tree_operador["columns"]:
    tree_operador.heading(col, text=col)
tree_operador.pack(fill='both', expand=True)

def cargar_datos():
    # Áreas
    from entities.area import Area
    session = get_areas.__globals__['session']
    for a in session.query(Area).all():
        tree_area.insert("", "end", values=(a.id, a.departamento, a.descripcion))

    # Supervisores
    supervisores = get_supervisores(session)
    for s in supervisores:
        tree_supervisor.insert("", "end", values=(s.id, s.nombre, s.telefono, s.correo, s.turno, s.area.departamento if s.area else "N/A"))

    # Operadores
    operadores = get_operadores(session)
    for o in operadores:
        tree_operador.insert("", "end", values=(
            o.id, o.nombre, o.sexo, o.fecha_ingreso, o.turno, o.salario,
            o.area.departamento if o.area else "N/A",
            o.supervisor.nombre if o.supervisor else "N/A"
        ))

cargar_datos()

root.mainloop()