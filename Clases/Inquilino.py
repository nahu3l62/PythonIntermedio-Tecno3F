class Inquilino:
    
    def __init__(self, nombre, apellido, dni, cuil, domicilio, email):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._cuil = cuil
        self._domicilio = domicilio
        self._email = email

    def getNombre(self):
        return self._nombre

    def setNombre(self, value):
        self._nombre = value

   
    def getApellido(self):
        return self._apellido


    def setApellido(self, value):
        self._apellido = value

 
    def getDni(self):
        return self._dni

    
    def setDni(self, value):
        self._dni = value

 
    def getCuil(self):
        return self._cuil

   
    def setCuil(self, value):
        self._cuil = value


    def getDomicilio(self):
        return self._domicilio

   
    def setDomicilio(self, value):
        self._domicilio = value

   
    def getEmail(self):
        return self._email

   
    def setEmail(self, value):
        self._email = value






        
        
