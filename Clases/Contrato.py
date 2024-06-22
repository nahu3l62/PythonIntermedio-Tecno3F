class Contrato: 
    def __init__(self, plazoMeses,idInquilino,idPropietario):
        self._plazoMeses = plazoMeses
        self._idInquilino = idInquilino
        self._idPropietario = idPropietario
        

    def getPlazoMeses(self):
        return self._plazoMeses

    def setPlazoMeses(self, value):
        self._plazoMeses = value

    def getIdInquilino(self):
        return self._idInquilino

    def setIdInquilino(self, value):
        self._idInquilino = value

    def getIdPropietario(self):
        return self._idPropietario

    def setIdPropietario(self, value):
        self._idPropietario = value

       
        