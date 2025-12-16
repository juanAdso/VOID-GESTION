#=======================================================================
# ARCHIVO: crudventas.py
# OBJETIVO: CRUD de ventas - VOID
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
# 2. FUNCIONES CRUD VENTAS
# -----------------------------------------

# CREATE
def crear_venta():
    id_cliente = entry_id_cliente.get()
    fecha = entry_fecha.get()
    total = entry_total.get()

    cursor = conexion.cursor()
    sql = """
    INSERT INTO ventas(id_cliente, fecha, total)
    VALUES (%s, %s, %s);
    """
    valores = (id_cliente, fecha, total)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Venta registrada correctamente")

# READ
def consultar_ventas():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ventas;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_venta():
    id_venta = entry_id_venta.get()
    id_cliente = entry_id_cliente.get()
    fecha = entry_fecha.get()
    total = entry_total.get()

    cursor = conexion.cursor()
    sql = """
    UPDATE ventas
    SET id_cliente = %s,
        fecha = %s,
        total = %s
    WHERE id_venta = %s;
    """
    valores = (id_cliente, fecha, total, id_venta)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Venta actualizada correctamente")

# DELETE
def eliminar_venta():
    id_venta = entry_id_venta.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM ventas WHERE id_venta = %s;"
    cursor.execute(sql, (id_venta,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Venta eliminada correctamente")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("CRUD Ventas - VOID")
ventana.geometry("650x550")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Venta").pack()
entry_id_venta = tk.Entry(ventana)
entry_id_venta.pack()

tk.Label(ventana, text="ID Cliente").pack()
entry_id_cliente = tk.Entry(ventana)
entry_id_cliente.pack()

tk.Label(ventana, text="Fecha").pack()
entry_fecha = tk.Entry(ventana)
entry_fecha.pack()

tk.Label(ventana, text="Total").pack()
entry_total = tk.Entry(ventana)
entry_total.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Registrar venta", command=crear_venta, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar ventas", command=consultar_ventas, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar venta", command=actualizar_venta, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar venta", command=eliminar_venta, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=70)
text_salida.pack(pady=10)

ventana.mainloop()
