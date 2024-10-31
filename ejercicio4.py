'''4- Herencia de clases
Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de
Animal las características y realice el sonido “guau guau”. La clase Gato que herede de
Animal las características y realice el sonido “Miau”. Del gato y el perro se debe poder
mostrar el sonido que realizan. Se debe crear la clase e implementarla.'''


class animal ():
    def __init__(self, nombre) :
        self.nombre = nombre
        return
class perro (animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def mostrar_sonido(self):
        print (f"el nombre del perro es {self.nombre} y el sonido que hace es guau guau")

class gato (animal):
    def __init__(self, nombre): 
        super().__init__(nombre)
    def mostrar_sonido(self):
        print (f"el nombre del gato es {self.nombre} y el sonido que hace es Miau")




