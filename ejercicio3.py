'''3- Clase para representar una Calculadora Crear una clase Calculadora que pueda calcular
suma, resta, multiplicación y división. Se debe crear la clase e implementarla.'''

class calculadora ():
    def __init__(self, numero1: int, numero2: int):
        self.numero1 = numero1
        self.numero2 = numero2
    def suma (self):
        print (f"la suma de los numero es : {self.numero1 + self.numero2}")
    def resta (self):
        print (f"la resta de los numero es : {self.numero1 - self.numero2}")
    def multiplicacion (self):
        print (f"la muliplicacion de los numero es : {self.numero1 * self.numero2}")
    def division (self):
        if (self.numero1 !=0 and self.numero2 !=0):
            print (f"la division de los numero es : {self.numero1 / self.numero2}")
        else:
            pass