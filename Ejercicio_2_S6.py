'''
En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
que tenga como atributos su nombre y su nota.
 Deberéis de definir los métodos para inicializar sus atributos,
 imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''


class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nota: {self.nota}')


    def resultado(self):
        if self.nota < 3:
            print('NO has Aprobado :(')
            print('-----------------')
        else:
            print('Has aprobado :)')
            print('-----------------')

# Creamos varios objetos de la clase Alumno
alumnoA = Alumno('James', 5)
alumnoB = Alumno('Cristina', 4)
alumnoC = Alumno('Geovany', 2)

# Imprimir los datos y resultados
alumnoA.imprimir_datos()
alumnoA.resultado()

alumnoB.imprimir_datos()
alumnoB.resultado()

alumnoC.imprimir_datos()
alumnoC.resultado()

