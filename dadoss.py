import random
import time
def azar_dados():
    semilla = time.time()
    aleatorio =random.seed(semilla)
    resul_maquina = 0
    resul_jugador = 0
    itera = 0
    while(itera < 6):
        if (itera%2 == 0):
            numero = int(random.random()*10)%6+1
            print ("Mi turno")
            resul_maquina += numero
            print (str(numero))
            print ("Mi puntuación es: "+str(resul_maquina))
            espera = raw_input("Presiona cualquier tecla para continuar: ")
            itera += 1
        else:
            numero = int(random.random()*10)%6+1
            print("Tu turno")
            resul_jugador += numero
            print (str(numero))
            print ("Tu puntuación es: "+str(resul_jugador))
            espera = raw_input("Presiona cualquier tecla para continuar: ")
            itera += 1
    if (resul_jugador < resul_maquina):
        print ("Yo gano")
    elif (resul_jugador == resul_maquina):
        print ("Hemos empatado")
    else:
        print ("Tu ganas")
    print("Tu puntuación es: "+str(resul_jugador))
    print("Mi puntuación es: "+str(resul_maquina))
azar_dados()
