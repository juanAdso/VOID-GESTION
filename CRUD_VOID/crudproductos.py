#=======================================================================
# ARCHIVO: crudproductos.py
# OBJETIVO: CRUD de productos - VOID
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
# 2. FUNCIONES CRUD PRODUCTOS
# -----------------------------------------

# CREATE
def crear_producto():
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    stock = entry_stock.get()

    cursor = conexion.cursor()
    sql = """
    INSERT INTO productos(nombre_producto, precio_producto, stock_producto)
    VALUES (%s, %s, %s);
    """
    valores = (nombre, precio, stock)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Producto creado correctamente")

# READ
def consultar_productos():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_producto():
    id_producto = entry_id.get()
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    stock = entry_stock.get()

    cursor = conexion.cursor()
    sql = """
    UPDATE productos
    SET nombre_producto = %s,
        precio_producto = %s,
        stock_producto = %s
    WHERE id_producto = %s;
    """
    valores = (nombre, precio, stock, id_producto)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Producto actualizado correctamente")

# DELETE
def eliminar_producto():
    id_producto = entry_id.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM productos WHERE id_producto = %s;"
    cursor.execute(sql, (id_producto,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Producto eliminado correctamente")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("CRUD Productos - VOID")
ventana.geometry("650x550")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Producto").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Nombre Producto").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Precio").pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Label(ventana, text="Stock").pack()
entry_stock = tk.Entry(ventana)
entry_stock.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Crear producto", command=crear_producto, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar productos", command=consultar_productos, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar producto", command=actualizar_producto, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar producto", command=eliminar_producto, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=70)
text_salida.pack(pady=10)

ventana.mainloop()
