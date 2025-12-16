#=======================================================================
# ARCHIVO: crudcategorias.py
# OBJETIVO: CRUD de categorías - VOID
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
# 2. FUNCIONES CRUD CATEGORÍAS
# -----------------------------------------

# CREATE
def crear_categoria():
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()

    cursor = conexion.cursor()
    sql = """
    INSERT INTO categorias(nombre_categoria, descripcion_categoria)
    VALUES (%s, %s);
    """
    valores = (nombre, descripcion)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Categoría creada correctamente")

# READ
def consultar_categorias():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categorias;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_categoria():
    id_categoria = entry_id.get()
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()

    cursor = conexion.cursor()
    sql = """
    UPDATE categorias
    SET nombre_categoria = %s,
        descripcion_categoria = %s
    WHERE id_categoria = %s;
    """
    valores = (nombre, descripcion, id_categoria)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Categoría actualizada correctamente")

# DELETE
def eliminar_categoria():
    id_categoria = entry_id.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM categorias WHERE id_categoria = %s;"
    cursor.execute(sql, (id_categoria,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Categoría eliminada correctamente")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("CRUD Categorías - VOID")
ventana.geometry("650x550")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Categoría").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Nombre Categoría").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Descripción").pack()
entry_descripcion = tk.Entry(ventana, width=40)
entry_descripcion.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Crear categoría", command=crear_categoria, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar categorías", command=consultar_categorias, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar categoría", command=actualizar_categoria, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar categoría", command=eliminar_categoria, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=70)
text_salida.pack(pady=10)

ventana.mainloop()
