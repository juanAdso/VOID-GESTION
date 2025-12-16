#=======================================================================
# ARCHIVO: crudusuarios.py
# OBJETIVO: CRUD de usuarios - VOID
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
# 2. FUNCIONES CRUD USUARIOS
# -----------------------------------------

# CREATE
def crear_usuario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    clave = entry_clave.get()

    cursor = conexion.cursor()
    sql = """
    INSERT INTO usuarios(nombre_usuario, correo_usuario, clave_usuario)
    VALUES (%s, %s, %s);
    """
    valores = (nombre, correo, clave)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Usuario creado correctamente")

# READ
def consultar_usuarios():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios;")

    text_salida.delete("1.0", tk.END)
    text_salida.insert(tk.END, "CAMPOS:\n")

    for campo in cursor.column_names:
        text_salida.insert(tk.END, f"{campo}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_usuario():
    id_usuario = entry_id.get()
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    clave = entry_clave.get()

    cursor = conexion.cursor()
    sql = """
    UPDATE usuarios
    SET nombre_usuario = %s,
        correo_usuario = %s,
        clave_usuario = %s
    WHERE id_usuario = %s;
    """
    valores = (nombre, correo, clave, id_usuario)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Usuario actualizado correctamente")

# DELETE
def eliminar_usuario():
    id_usuario = entry_id.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM usuarios WHERE id_usuario = %s;"
    cursor.execute(sql, (id_usuario,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Usuario eliminado correctamente")

# -----------------------------
# 3. INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("CRUD Usuarios - VOID")
ventana.geometry("650x550")

# ======= ENTRADAS ======
tk.Label(ventana, text="ID Usuario").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana)
entry_correo.pack()

tk.Label(ventana, text="Clave").pack()
entry_clave = tk.Entry(ventana, show="*")
entry_clave.pack()

# ====== BOTONES ======
tk.Button(ventana, text="Crear usuario", command=crear_usuario, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="Consultar usuarios", command=consultar_usuarios, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar usuario", command=actualizar_usuario, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar usuario", command=eliminar_usuario, bg="#F44336", fg="white").pack(pady=5)

# ====== SALIDA ======
text_salida = tk.Text(ventana, height=12, width=70)
text_salida.pack(pady=10)

ventana.mainloop()
