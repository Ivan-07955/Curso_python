import random
import time


def aleatorio():
    semilla=time.time()#carga el tiempo transcurrido desde una referencia (epoch) dada
    random.seed(semilla) #inicializa el generador de números aleatorios. De este modo
    #cada vez que ejecutemos el programa consulta la lista de números aleatorios
    #desde una posición distinta
   
    for cont in range(1,11):
        numero=int(random.random()*10)%10
        print(numero)#generamos un número aleatorio y lo sacamos por pantalla

aleatorio()
