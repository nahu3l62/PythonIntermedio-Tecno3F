import sqlite3
from Clases.Contrato import Contrato


def conectar():
    conexion = sqlite3.connect("ddbb/database.db")
    return conexion

# ----------------------------------------------------------------------------

# READ


def consultaContrato():
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = "SELECT * FROM CONTRATO"
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    finally:
        cone.close()


# ----------------------------------------------------------------------------

# CREATE

def guardarContrato(Contrato):
    try:
        cone = conectar()
        cur = cone.cursor()
        cur.execute("INSERT INTO CONTRATO (plazoMeses,idInquilino,idPropietario) VALUES (?, ?, ?)",
                    (Contrato.getPlazoMeses(), Contrato.getIdInquilino(), Contrato.getIdPropietario()))
        cone.commit()
    finally:
        cone.close()


# ----------------------------------------------------------------------------

# DELETE

def borrarContrato(id):
    try:
        cone = conectar()
        cur = cone.cursor()
        sql = f"DELETE FROM CONTRATO WHERE IDCONTRATO = {id}"
        cur.execute(sql)
        cone.commit()
    except sqlite3.Error as er:
        print(f"Error inesperado. {er}")
    finally:
        if 1 == cur.rowcount:
            print(f"El Contrato id {id} se borro con exito.")
        else:
            print(f"El Contrato id {id} no se borro")
        cone.close()


# ----------------------------------------------------------------------------

# UPDATE

def actualizarContrato(plazoMeses):

    try:
        cone = conectar()
        cur = cone.cursor()
        sql = f"UPDATE CONTRATO SET plazoMeses=(?) WHERE IDCONTRATO = {id}"
        cur.execute(sql, plazoMeses)
        cone.commit()
    except sqlite3.Error as er:
        print(f"Error inesperado. {er}")
    finally:
        if 1 == cur.rowcount:
            print(f"El Contrato id {id} se actualizo con exito.")
        else:
            print(f"El Contrato id {id} no se actualizo")
        cone.close()