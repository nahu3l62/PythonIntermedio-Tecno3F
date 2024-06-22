import sqlite3
from Clases.Propietario import Propietario


def conectar():
    conexion = sqlite3.connect("ddbb/database.db")
    return conexion

# ----------------------------------------------------------------------------

# READ


def consultaPropietario():
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = "SELECT * FROM PROPIETARIO"
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    finally:
        cone.close()

# ----------------------------------------------------------------------------

# CREATE


def guardarPropietario(Propietario):
    try:
        cone = conectar()
        cur = cone.cursor()
        cur.execute("INSERT INTO PROPIETARIO (nombre,apellido,dni,cuil,domicilio,email) VALUES (?, ?, ?, ?, ?, ?)", (Propietario.getNombre(
        ), Propietario.getApellido(), Propietario.getDni(), Propietario.getCuil(), Propietario.getDomicilio(), Propietario.getEmail()))
        cone.commit()
    finally:
        cone.close()


# ----------------------------------------------------------------------------

# DELETE


def borrarPropietario(id):
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = f"DELETE FROM PROPIETARIO WHERE IDPROPIETARIO = {id}"
        cur.execute(sql)
        cone.commit()
    except sqlite3.Error as er:
        print(f"Error inesperado. {er}")
    finally:
        if 1 == cur.rowcount:
            print(f"El propietario id {id} se borro con exito.")
        else:
            print(f"El propietario id {id} no se borro")
        cone.close()

# ----------------------------------------------------------------------------

# UPDATE


def actualizarPropietario(Propietario, id):
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = f"UPDATE PROPIETARIO SET nombre=(?), apellido=(?), dni=(?), cuil=(?), domicilio=(?), email=(?) WHERE IDPROPIETARIO = {id}"
        cur.execute(sql, (Propietario.getNombre(
        ), Propietario.getApellido(), Propietario.getDni(), Propietario.getCuil(), Propietario.getDomicilio(), Propietario.getEmail()))
        cone.commit()
    except sqlite3.Error as er:
        print(f"Error inesperado. {er}")
    finally:
        if 1 == cur.rowcount:
            print(f"El propietario id {id} se actualizo con exito.")
        else:
            print(f"El propietario id {id} no se actualizo")
        cone.close()