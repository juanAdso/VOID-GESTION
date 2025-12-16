#=======================================================================
# ARCHIVO: crudinventario.py
# OBJETIVO: CRUD de inventario - VOID
# ======================================================================= 

import mysql.connector
import tkinter as tk
from tkinter import messagebox
from datetime import date

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
# 2. FUNCIONES CRUD INVENTARIO
# -----------------------------------------

# CREATE
def crear_registro():
    id_producto = entry_id_producto.get()
    cantidad = entry_cantidad.get()
    fecha = date.today()

    cursor = conexion.cursor()
    sql = """
    INSERT INTO inventario(id_producto, cantidad, fecha_actualizacion)
    VALUES (%s, %s, %s);
    """
    valores = (id_producto, cantidad, fecha)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Registro de inventario creado")

# READ
def consultar_inventario():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM inventario;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_inventario():
    id_inventario = entry_id.get()
    id_producto = entry_id_producto.get()
    cantidad = entry_cantidad.get()
    fecha = date.today()

    cursor = conexion.cursor()
    sql = """
    UPDATE inventario
    SET id_producto = %s,
        cantidad = %s,
        fecha_actualizacion = %s
    WHERE id_inventario = %s;
    """
    valores = (id_producto, cantidad, fecha, id_inventario)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Inventario actualizado correctamente")

# DELETE
def eliminar_registro():
    id_inventario = entry_id.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM inventario WHERE id_inventario = %s;"
    cursor.execute(sql, (id_inventario,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Registro de inventario eliminado")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("Inventario - VOID")
ventana.geometry("650x550")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Inventario").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Cantidad").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Registrar inventario", command=crear_registro, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar inventario", command=consultar_inventario, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar inventario", command=actualizar_inventario, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar registro", command=eliminar_registro, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=70)
text_salida.pack(pady=10)

ventana.mainloop()
