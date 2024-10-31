'''2 - Clase para representar un Rectángulo Crear una clase rectángulo que tenga las
características base y altura. Del rectángulo se debe poder calcular el área y el perímetro.
Se debe crear la clase e implementarla.'''

class rectangulo () : 
    def __init__(self, base: int, altura: int):

        self.base = base
        self.altura = altura

    def calcular_area (self):
        print(f"el area del rectangulo es: {self.base * self. altura}")

    def calcular_perimetro (self):
        
        print (f"el perimetro del rectangulo es : {2* (self.base + self. altura)}")

