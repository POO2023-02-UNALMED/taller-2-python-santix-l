class Asiento:

    def __init__(self, color, precio, registro):

        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):

        if color == "rojo" or color == "negro" or color == "amarillo" or color == "verde" or color == "blanco":

            self.color = color

class Motor:

    def __init__(self, numeroCilindros, tipo, registro):

        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):

        self.registro = registro

    def asignarTipo(self, tipo):

        if tipo == "electrico" or tipo == "gasolina":

            self.tipo = tipo

class Auto:

    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, registro, marca, motor):

        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.registro = registro
        self.marca = marca
        self.Motor = motor

    def cantidadAsientos(self):

        nAsientos = 0

        for asiento in self.asientos:

            if asiento != None:
                nAsientos += 1

        return nAsientos
    
    def verificarIntegridad(self):

        if self.registro == self.Motor.registro:

            for i in self.asientos:

                if i != None and i.registro != self.registro:

                    return "Las piezas no son originales"
            
            return "Auto original"
        
        else: return "Las piezas no son originales"

            








    