class Auto:
    def __init__(self, color, modelo, llantas, puertas, velocidades):
        self.color = color
        self.modelo = modelo
        self.llantas = llantas
        self.puertas = puertas
        self.velocidades = velocidades

    def mostrar_datos(self):
        print(f"color:{self.color}, modelo:{self.modelo}, llantas:{self.llantas}, puertas:{self.puertas}, vel:{self.velocidades}")

"""
ENCAPSULAMIENTO
"""
class Persona:
    # campo contrasenia como privado
    __ci = ""
    def __init__(self,nombre):
        self.nombre = nombre

    def set_ci(self, ci):
        self.__ci = ci
    
    def get_ci(self):
        return self.__ci

    def mostrar_datos(self):
        print(f"usuario:{self.nombre}, ci:{self.get_ci()}")

"""
HERENCIA
"""

class Empleado(Persona):
    __sueldo = 0
    
    def __init__(self, cargo):
        self.cargo = cargo

    def set_sueldo(self,sueldo):
        self.__sueldo = sueldo
    
    def get_sueldo(self):
        return self.__sueldo
    def mostrar_datos(self):
        print(f"usuario:{self.nombre}, ci:{self.get_ci()}, cargo:{self.cargo}, sueldo:{self.get_sueldo()}")
