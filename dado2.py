#Vamos a hacer un ejercio que genere al azar un número entre 1 y 6.
import random
import time

def dado():
    semilla=time.time()
    print("semilla= "+str(semilla))
    random.seed(semilla)
    respuesta=raw_input("¿Quieres que tire un dado 100 veces (S/N)? ")
    for cont in range(1,101):
        tirada=int(1+(random.random()*10)%6)
        print("Ha salido un "+str(tirada))
    print("Se acabó el juego")

dado()
