#Haz un programa que lea el nombre, los apellidos y la edad de nacimeinto de
#un usuario y devuelva una cadena con:
#3 primeras letras del apellido 1
#3 primeras letras del segundo apellido
#3 primeras letras del nombre
#2 �ltimas cifras del a�o de nacimiento
#EJEMPLO Antonio L�pez Polo 1970
# -> L�pPolAnt70

def usuario_nombre():
    nombre=raw_input("Nombre: ")
    apellido1=raw_input("Primer apellido: ")
    apellido2=raw_input("Segundo apellido: ")
    nacimiento=raw_input("Fecha nacimiento (dd/mm/aaaa): ")
    usuario=apellido1[0:3]+apellido1[0:3]+nombre[0:3]+nacimiento[8:10]
    print("Usuario: "+usuario)

usuario_nombre()
