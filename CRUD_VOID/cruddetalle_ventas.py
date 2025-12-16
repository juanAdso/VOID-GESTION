#=======================================================================
# ARCHIVO: crudetalleventas.py
# OBJETIVO: CRUD de detalle de ventas - VOID
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
# 2. FUNCIONES CRUD DETALLE VENTAS
# -----------------------------------------

# CREATE
def crear_detalle():
    id_venta = entry_id_venta.get()
    id_producto = entry_id_producto.get()
    cantidad = int(entry_cantidad.get())
    precio = float(entry_precio.get())
    subtotal = cantidad * precio

    cursor = conexion.cursor()
    sql = """
    INSERT INTO detalle_ventas(id_venta, id_producto, cantidad, precio_unitario, subtotal)
    VALUES (%s, %s, %s, %s, %s);
    """
    valores = (id_venta, id_producto, cantidad, precio, subtotal)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Detalle de venta registrado")

# READ
def consultar_detalles():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM detalle_ventas;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_detalle():
    id_detalle = entry_id_detalle.get()
    id_venta = entry_id_venta.get()
    id_producto = entry_id_producto.get()
    cantidad = int(entry_cantidad.get())
    precio = float(entry_precio.get())
    subtotal = cantidad * precio

    cursor = conexion.cursor()
    sql = """
    UPDATE detalle_ventas
    SET id_venta = %s,
        id_producto = %s,
        cantidad = %s,
        precio_unitario = %s,
        subtotal = %s
    WHERE id_detalle = %s;
    """
    valores = (id_venta, id_producto, cantidad, precio, subtotal, id_detalle)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Detalle de venta actualizado")

# DELETE
def eliminar_detalle():
    id_detalle = entry_id_detalle.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM detalle_ventas WHERE id_detalle = %s;"
    cursor.execute(sql, (id_detalle,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Detalle de venta eliminado")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("Detalle de Ventas - VOID")
ventana.geometry("700x600")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Detalle").pack()
entry_id_detalle = tk.Entry(ventana)
entry_id_detalle.pack()

tk.Label(ventana, text="ID Venta").pack()
entry_id_venta = tk.Entry(ventana)
entry_id_venta.pack()

tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Cantidad").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

tk.Label(ventana, text="Precio Unitario").pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Agregar detalle", command=crear_detalle, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar detalles", command=consultar_detalles, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar detalle", command=actualizar_detalle, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar detalle", command=eliminar_detalle, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=80)
text_salida.pack(pady=10)

ventana.mainloop()
