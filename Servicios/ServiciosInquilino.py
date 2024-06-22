import sqlite3
from Clases.Inquilino import *


def conectar():
    conexion = sqlite3.connect("ddbb/database.db")
    return conexion


# ----------------------------------------------------------------------------

# READ


def consultaInquilino():
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = "SELECT * FROM INQUILINO"
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    finally:
        cone.close()


def mostrarInquilino():
    resultado = consultaInquilino()
    print(resultado)
    

# ----------------------------------------------------------------------------

# CREATE

def guardarInquilino(Inquilino):
    try:
        cone = conectar()
        cur = cone.cursor()
        cur.execute("INSERT INTO INQUILINO (nombre,apellido,dni,cuil,domicilio,email) VALUES (?, ?, ?, ?, ?, ?)", (Inquilino.getNombre(
        ), Inquilino.getApellido(), Inquilino.getDni(), Inquilino.getCuil(), Inquilino.getDomicilio(), Inquilino.getEmail()))
        cone.commit()
    finally:
        cone.close()

# ----------------------------------------------------------------------------

# DELETE

def borrarInquilino(id):
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = f"DELETE FROM INQUILINO WHERE IDINQUILINO = {id}"
        cur.execute(sql)
        cone.commit()
    except sqlite3.Error as er:
        print(f"Error inesperado. {er}")
    finally:
        if 1 == cur.rowcount:
            print(f"El inquilino id {id} se borro con exito.")
        else:
            print(f"El inquilino id {id} no se borro")
        cone.close()


# ----------------------------------------------------------------------------

# UPDATE

def actualizarInquilino(Inquilino, id):
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = f"UPDATE INQUILINO SET nombre=(?), apellido=(?), dni=(?), cuil=(?), domicilio=(?), email=(?) WHERE IDINQUILINO = {id}"
        cur.execute(sql, (Inquilino.getNombre(
        ), Inquilino.getApellido(), Inquilino.getDni(), Inquilino.getCuil(), Inquilino.getDomicilio(), Inquilino.getEmail()))
        cone.commit()
    except sqlite3.Error as er:
        print(f"Error inesperado. {er}")
    finally:
        if 1 == cur.rowcount:
            print(f"El inquilino id {id} se actualizo con exito.")
        else:
            print(f"El inquilino id {id} no se actualizo")
        cone.close()
