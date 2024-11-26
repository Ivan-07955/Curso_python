#Vamos a hacer un ejercicio que genere al azar un número entre 1 y 6.
import random
def dado():
    respuesta=raw_input("¿Quieres que tire un dado (S/N)? ")
    while(respuesta=="S"):
        tirada=random.random()
        print("Ha salido un "+str(tirada))
        respuesta=raw_input("¿Quieres volver a tirar el dado (S/N)? ")
    print("Se acabó el juego")

dado()
