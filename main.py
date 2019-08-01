from helpers import Auto, Persona, Empleado

def main():
    auto = Auto(color='Rojo', modelo="BMW", llantas=4, puertas=2, velocidades=6)
    auto.mostrar_datos()

    persona = Persona(nombre='identiclla')
    #print(persona.__contrasenia) no podemos acceder
    persona.set_ci(2000)
    persona.mostrar_datos()

    empleado = Empleado(cargo='Gerente')
    empleado.nombre = 'Jose'
    empleado.set_ci(12653415)
    empleado.set_sueldo(5000)
    empleado.mostrar_datos()
if __name__ == "__main__":
    main()