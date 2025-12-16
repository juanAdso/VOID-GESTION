#=======================================================================
# ARCHIVO: conexion_abierta.py
# OBJETIVO: Conectar a Mysql y mantener
#           la conexion abierta
# ======================================================================= 

import mysql.connector
import tkinter as tk
from tkinter import messagebox

#Creamos la conexión sin cerrarla
conexion = mysql.connector.connect(
    host="localhost",                                 # Servidor Mysql
    user="root",                                       # Usuario de Mysql
    password="",                                       # Contraseña (vacía si no tiene)
    database="mer_void"                          # Base de datos a conectar
)

if conexion.is_connected():
    print("conexion establecida correctamente")


# -----------------------------------------
# 2. FUNCIONES CRUD
# -----------------------------------------

#CREATE
def crear_rol():
    nombre = entry_nombre.get()

    cursor = conexion.cursor()
    sql = """
    INSERT INTO roles(nombre_rol_roles)
    VALUES (%s);
    """
    valores = (nombre)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Rol creado correctamente")

# READ
def consultar_rol():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM roles;")

    text_salida.delete("1.0", tk.END) # limpiar pantalla
    
    text_salida.insert(tk.END, "CAMPOS:")
    
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\n REGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")

# UPDATE
def actualizar_rol():
    id_rol = entry_id.get()
    nuevo_nombre = entry_nombre.get()

    cursor = conexion.cursor()
    sql = """
    UPDATE roles SET nombre_rol_roles = %s
    WHERE id_rol = %s;
    """
    valores = (nuevo_nombre, id_rol)

    cursor.execute(sql, valores)
    conexion.commit()

    messagebox.showinfo("Éxito", "Rol actualizado correctamente")


# DELETE
def eliminar_rol():
    id_rol = entry_id.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM roles WHERE id_rol = %s;"
    cursor.execute(sql, (id_rol,))
    conexion.commit()

    messagebox.showinfo("Éxito", "Rol eliminado correctamente")


# -----------------------------
# 3. INTERFAZ GRAFICA TKINTER
# -----------------------------
ventana = tk.Tk()
ventana.title("Crud roles")
ventana.geometry("600x500")


# ======= ENTRADAS ======
tk.Label(ventana, text="ID rol").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()


# ====== BOTONES ======
tk.Button(ventana, text="crear rol", command=crear_rol, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(ventana, text="consultar rol", command=consultar_rol, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="actualizar rol", command=actualizar_rol, bg="#FFC107").pack(pady=5)
tk.Button(ventana, text="Eliminar rol", command=eliminar_rol, bg="#F44336", fg="white").pack(pady=5)


# ============ CAJA DE TEXTO PARA MOSTRAR RESULTADOS
text_salida =tk.Text(ventana, height=10, width=60)
text_salida.pack(pady=10)

ventana.mainloop()
