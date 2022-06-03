# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas

class Vehiculo:
    color = 'Negro'
    ruedas = 4
    puertas = 4


# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# cilindrada
class Coche(Vehiculo):
    velocidad = 80
    cilindraje = 4000


# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

coche1 = Coche()

print(f'Color: {coche1.color}')
print(f'Ruedas: {coche1.ruedas}')
print(f'Puertas: {coche1.puertas}')
print(f'Velocidad: {coche1.velocidad}')
print(f'Cilindraje: {coche1.cilindraje}')

