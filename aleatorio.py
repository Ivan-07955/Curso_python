import random
import time


def aleatorio():
    semilla=time.time()#carga el tiempo transcurrido desde una referencia (epoch) dada
    random.seed(semilla) #inicializa el generador de n�meros aleatorios. De este modo
    #cada vez que ejecutemos el programa consulta la lista de n�meros aleatorios
    #desde una posici�n distinta
   
    for cont in range(1,11):
        numero=int(random.random()*10)%10
        print(numero)#generamos un n�mero aleatorio y lo sacamos por pantalla

aleatorio()
