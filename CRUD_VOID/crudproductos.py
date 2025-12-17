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
    database="void"
)

if conexion.is_connected():
    print("Conexión establecida correctamente")

# -----------------------------------------
# 2. FUNCIONES CRUD PRODUCTOS
# -----------------------------------------

# CREATE
def crear_producto():
    nombre = entry_nombre.get()
    tipo = entry_tipo.get()
    descripcion = entry_descripcion.get()
    imagen = entry_imagen.get()
    id_categoria = entry_id_categoria.get()

    if nombre == "" or tipo == "" or id_categoria == "":
        messagebox.showwarning("Advertencia", "Nombre, tipo y categoría son obligatorios")
        return

    cursor = conexion.cursor()
    sql = """
    INSERT INTO productos(nombre_producto, tipo_prenda, descripcion_producto, imagen_producto, id_categoria)
    VALUES (%s, %s, %s, %s, %s);
    """
    valores = (nombre, tipo, descripcion, imagen, id_categoria)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Producto registrado correctamente")

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
    id_producto = entry_id_producto.get()
    nombre = entry_nombre.get()
    tipo = entry_tipo.get()
    descripcion = entry_descripcion.get()
    imagen = entry_imagen.get()
    id_categoria = entry_id_categoria.get()

    if id_producto == "":
        messagebox.showwarning("Advertencia", "Debe ingresar el ID del producto")
        return

    cursor = conexion.cursor()
    sql = """
    UPDATE productos
    SET nombre_producto = %s,
        tipo_prenda = %s,
        descripcion_producto = %s,
        imagen_producto = %s,
        id_categoria = %s
    WHERE id_producto = %s;
    """
    valores = (nombre, tipo, descripcion, imagen, id_categoria, id_producto)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Producto actualizado correctamente")

# DELETE
def eliminar_producto():
    id_producto = entry_id_producto.get()

    if id_producto == "":
        messagebox.showwarning("Advertencia", "Debe ingresar el ID del producto")
        return

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
ventana.geometry("700x580")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Nombre del Producto").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Tipo de Prenda").pack()
entry_tipo = tk.Entry(ventana)
entry_tipo.pack()

tk.Label(ventana, text="Descripción").pack()
entry_descripcion = tk.Entry(ventana)
entry_descripcion.pack()

tk.Label(ventana, text="Imagen (ruta o URL)").pack()
entry_imagen = tk.Entry(ventana)
entry_imagen.pack()

tk.Label(ventana, text="ID Categoría").pack()
entry_id_categoria = tk.Entry(ventana)
entry_id_categoria.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Registrar producto", command=crear_producto, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar productos", command=consultar_productos, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar producto", command=actualizar_producto, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar producto", command=eliminar_producto, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=80)
text_salida.pack(pady=10)

ventana.mainloop()
