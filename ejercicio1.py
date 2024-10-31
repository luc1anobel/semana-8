'''1 -Clase para representar un Libro
Crear una clase Libro que tenga las características título, autor y año de publicación. Del
libro se debe poder obtener información, mostrando por mensaje todos sus datos. Se debe
crear la clase e implementarla.'''


class libro ():
    def __init__ (self, titulo: str, autor: str, año_de_publicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion
    
    def obtener_informacion (self):
        print (f"el titulo del libro es: {self.titulo}\n el autor del libro es: {self.autor}\n el año en el que se publico es: {self.año_de_publicacion}")
        return
    

