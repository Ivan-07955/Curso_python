#Leo cinco números y me dice cuál es el menor
def menor():
    menor=int(input("Dime un número entero mayor que cero: "))

    #inicializar la variable.
    for cont in range(1,6):
        numero=int(input("Dime un número entero mayor que cero: "))
        if(numero<menor):
            menor=numero
    print("EL Menor ES "+str(menor))

menor()
