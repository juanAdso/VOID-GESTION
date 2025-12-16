#=======================================================================
# ARCHIVO: crudclientes.py
# OBJETIVO: CRUD de clientes - VOID
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
# 2. FUNCIONES CRUD CLIENTES
# -----------------------------------------

# CREATE
def crear_cliente():
    nombre = entry_nombre.get()

    cursor = conexion.cursor()
    sql = """
    INSERT INTO clientes(nombre_cliente)
    VALUES (%s);
    """
    valores = (nombre,)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Cliente creado correctamente")

# READ
def consultar_clientes():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_cliente():
    id_cliente = entry_id.get()
    nuevo_nombre = entry_nombre.get()

    cursor = conexion.cursor()
    sql = """
    UPDATE clientes
    SET nombre_cliente = %s
    WHERE id_cliente = %s;
    """
    valores = (nuevo_nombre, id_cliente)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Cliente actualizado correctamente")

# DELETE
def eliminar_cliente():
    id_cliente = entry_id.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM clientes WHERE id_cliente = %s;"
    cursor.execute(sql, (id_cliente,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Cliente eliminado correctamente")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("CRUD Clientes - VOID")
ventana.geometry("600x500")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Cliente").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Nombre Cliente").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Crear cliente", command=crear_cliente, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar clientes", command=consultar_clientes, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar cliente", command=actualizar_cliente, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar cliente", command=eliminar_cliente, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=10, width=60)
text_salida.pack(pady=10)

ventana.mainloop()

