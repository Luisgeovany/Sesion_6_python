# Clases

# clase ave
class Ave:
    patas = 2
    alas = True

    def volar(self):
        return 'Puedo volar'

    def cantar(self):
        return 'Puedo cantar'


# Instancias de la clase
ganso = Ave()
print(ganso.volar())
print(ganso.alas)

loro = Ave()
print(loro.cantar())
print(loro.volar())


# Herencia

class Gallinas(Ave):
    pone_huevos = True

    def cacarea(self):
        return 'La gallina Cacarea '


print('------------------------------------------')

gall1 = Gallinas()
print(gall1.alas)
print(gall1.cacarea())

print('------------------------------------------')

gall2 = Gallinas()
print(gall2.pone_huevos)
print((gall2.alas))

print('------------------------------------------')


# Constructor

class Vehiculo():
    marca = None
    color = None
    gama = None

    def __init__(self, gama):
        self.color = 'Rojo'
        self.marca = 'Ferrari'
        self.gama = gama

    def automatico(self):
        return('Este vehiculo es de encendido Automatico')


auto1 = Vehiculo('Alta')

print(auto1.gama)
print(auto1.color)
print(auto1.automatico())
