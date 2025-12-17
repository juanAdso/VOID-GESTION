#=======================================================================
# ARCHIVO: crudcontactos.py
# OBJETIVO: CRUD de contactos - VOID
# =======================================================================

import mysql.connector
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# 1. CONEXIÓN A MYSQL
# -----------------------------
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="void"
)

if conexion.is_connected():
    print("Conexión establecida correctamente")

# -----------------------------------------
# 2. FUNCIONES CRUD CONTACTOS
# -----------------------------------------

# CREATE
def crear_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()

    if nombre == "" or telefono == "":
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    cursor = conexion.cursor()
    sql = """
    INSERT INTO contactos(nombre_contacto, telefono_contacto)
    VALUES (%s, %s);
    """
    valores = (nombre, telefono)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Contacto registrado correctamente")

# READ
def consultar_contactos():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contactos;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_contacto():
    id_contacto = entry_id_contacto.get()
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()

    if id_contacto == "":
        messagebox.showwarning("Advertencia", "Debe ingresar el ID del contacto")
        return

    cursor = conexion.cursor()
    sql = """
    UPDATE contactos
    SET nombre_contacto = %s,
        telefono_contacto = %s
    WHERE id_contacto = %s;
    """
    valores = (nombre, telefono, id_contacto)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Contacto actualizado correctamente")

# DELETE
def eliminar_contacto():
    id_contacto = entry_id_contacto.get()

    if id_contacto == "":
        messagebox.showwarning("Advertencia", "Debe ingresar el ID del contacto")
        return

    cursor = conexion.cursor()
    sql = "DELETE FROM contactos WHERE id_contacto = %s;"
    cursor.execute(sql, (id_contacto,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Contacto eliminado correctamente")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("CRUD Contactos - VOID")
ventana.geometry("650x500")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Contacto").pack()
entry_id_contacto = tk.Entry(ventana)
entry_id_contacto.pack()

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Teléfono").pack()
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Registrar contacto", command=crear_contacto, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar contactos", command=consultar_contactos, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar contacto", command=actualizar_contacto, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar contacto", command=eliminar_contacto, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=70)
text_salida.pack(pady=10)

ventana.mainloop()