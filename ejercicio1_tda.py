'''1- Cargar secuencialmente una lista de alumnos, cada alumno
debe ser un diccionario con cuatro claves: nombre, apellido, edad y
la clave curso que posea de valor una tupla con el curso.'''

# Lista para almacenar los alumnos 
lista_de_alumnos = [] 
def agregar_alumno():
    res = "si"
    while res == "si":
        nombre = input("Ingrese el nombre del alumno: ") 
        apellido = input("Ingrese el apellido del alumno: ") 
        edad = int(input("Ingrese la edad del alumno: ")) 
        curso = input("Ingrese la materia del alumno: ") 
        curso = (curso, 117)
        alumno = (f"nombre: {nombre}, apellido: {apellido}, edad: {edad}, curso: {curso}")
        lista_de_alumnos.append(alumno) 
        res = input("desea seguir ingresando alumnos(si-no) : ")


agregar_alumno() 

for alumno in lista_de_alumnos: 
    print(alumno)