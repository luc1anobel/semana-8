'''5- Encapsulamiento Crear una clase Cuenta Bancaria que tenga las características titular y
saldo encapsulado. De la cuenta bancaria se puede obtener el saldo, depositar o retirar (en
cada caso imprimir que fue exitoso). Se debe crear la clase e implementarla.
CADENA DE CARACTERES-Métodos'''
class cuenta_bancaria():
    def __init__(self,titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def obtener_saldo (self):
        print (f"el saldo de la cuenta de {self.titular} es de : {self.__saldo}")
    def depositar (self):
        deposito = int(input("ingrese la cantidad que desea depositar: "))
        self.__saldo += deposito
        print(f"deposito Exitoso. el saldo final de {self.titular} es de {self.__saldo}") 
    def retirar (self) :
        res="si"
        retirar = int(input("ingrese la cantidad que desea retirar: "))
        while res == "si":
            if retirar >= self.__saldo:
                retirar = int(input("Error fondos insuficiente. \ningrese una cantidad menor a la ingresada anterior mente: "))
            else:
                self.__saldo -= retirar
                print(f"retiro exitoso. el saldo final de {self.titular} es de {self.__saldo}") 
                res = "no"