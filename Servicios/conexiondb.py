import sqlite3

class ConexionDB():
    def __init__(self):
        self.nombre_db = 'ddbb/database.db'
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()
        
    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()
        
