#=======================================================================
# ARCHIVO: crudsolicitudes_diseno.py
# OBJETIVO: CRUD de solicitudes de diseño - VOID
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
# 2. FUNCIONES CRUD SOLICITUDES DE DISEÑO
# -----------------------------------------

# CREATE
def crear_solicitud():
    id_contacto = entry_id_contacto.get()
    id_producto = entry_id_producto.get()
    descripcion = entry_descripcion.get("1.0", tk.END).strip()

    if id_contacto == "" or id_producto == "" or descripcion == "":
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    cursor = conexion.cursor()
    sql = """
    INSERT INTO solicitudes_diseno(id_contacto, id_producto, descripcion_diseno)
    VALUES (%s, %s, %s);
    """
    valores = (id_contacto, id_producto, descripcion)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Solicitud registrada correctamente")

# READ
def consultar_solicitudes():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM solicitudes_diseno;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_solicitud():
    id_solicitud = entry_id_solicitud.get()
    id_contacto = entry_id_contacto.get()
    id_producto = entry_id_producto.get()
    descripcion = entry_descripcion.get("1.0", tk.END).strip()

    if id_solicitud == "":
        messagebox.showwarning("Advertencia", "Debe ingresar el ID de la solicitud")
        return

    cursor = conexion.cursor()
    sql = """
    UPDATE solicitudes_diseno
    SET id_contacto = %s,
        id_producto = %s,
        descripcion_diseno = %s
    WHERE id_solicitud = %s;
    """
    valores = (id_contacto, id_producto, descripcion, id_solicitud)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Solicitud actualizada correctamente")

# DELETE
def eliminar_solicitud():
    id_solicitud = entry_id_solicitud.get()

    if id_solicitud == "":
        messagebox.showwarning("Advertencia", "Debe ingresar el ID de la solicitud")
        return

    cursor = conexion.cursor()
    sql = "DELETE FROM solicitudes_diseno WHERE id_solicitud = %s;"
    cursor.execute(sql, (id_solicitud,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Solicitud eliminada correctamente")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("CRUD Solicitudes de Diseño - VOID")
ventana.geometry("700x600")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Solicitud").pack()
entry_id_solicitud = tk.Entry(ventana)
entry_id_solicitud.pack()

tk.Label(ventana, text="ID Contacto").pack()
entry_id_contacto = tk.Entry(ventana)
entry_id_contacto.pack()

tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Descripción del Diseño").pack()
entry_descripcion = tk.Text(ventana, height=5, width=50)
entry_descripcion.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Registrar solicitud", command=crear_solicitud, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar solicitudes", command=consultar_solicitudes, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar solicitud", command=actualizar_solicitud, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar solicitud", command=eliminar_solicitud, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=80)
text_salida.pack(pady=10)

ventana.mainloop()