#=======================================================================
# ARCHIVO: crudproveedores.py
# OBJETIVO: CRUD de proveedores - VOID
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
    database="mer_void"
)

if conexion.is_connected():
    print("Conexión establecida correctamente")

# -----------------------------------------
# 2. FUNCIONES CRUD PROVEEDORES
# -----------------------------------------

# CREATE
def crear_proveedor():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()

    cursor = conexion.cursor()
    sql = """
    INSERT INTO proveedores(nombre_proveedor, telefono_proveedor, correo_proveedor)
    VALUES (%s, %s, %s);
    """
    valores = (nombre, telefono, correo)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Proveedor creado correctamente")

# READ
def consultar_proveedores():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proveedores;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_proveedor():
    id_proveedor = entry_id.get()
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()

    cursor = conexion.cursor()
    sql = """
    UPDATE proveedores
    SET nombre_proveedor = %s,
        telefono_proveedor = %s,
        correo_proveedor = %s
    WHERE id_proveedor = %s;
    """
    valores = (nombre, telefono, correo, id_proveedor)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Proveedor actualizado correctamente")

# DELETE
def eliminar_proveedor():
    id_proveedor = entry_id.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM proveedores WHERE id_proveedor = %s;"
    cursor.execute(sql, (id_proveedor,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Proveedor eliminado correctamente")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("CRUD Proveedores - VOID")
ventana.geometry("650x550")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Proveedor").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Nombre Proveedor").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Teléfono").pack()
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana)
entry_correo.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Crear proveedor", command=crear_proveedor, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar proveedores", command=consultar_proveedores, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar proveedor", command=actualizar_proveedor, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar proveedor", command=eliminar_proveedor, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=70)
text_salida.pack(pady=10)

ventana.mainloop()
