# Inicializamos la clase Vehiculo
class Vehiculo():
    # Constructor
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return 'Color {}, {} ruedas'.format(self.color, self.ruedas, self.puertas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindraje):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return 'Color {}, {} km/h, {} ruedas, {} puertas, {} cc'.format(self.color, self.velocidad, self.ruedas,
                                                                        self.puertas, self.cilindraje)


coche = Coche('Rojo', 4, 4, 100, 1600)

print(coche)
