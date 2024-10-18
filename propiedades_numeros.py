#Leo cinco números y me devuelve el mayor, el menor, la suma de todos la media y la resta entre el mayor y el menor.
def propiedades_numeros():
    numero=int(input("Dime un número entero mayor que cero: "))
    suma=0
    mayor=numero
    menor=numero
    for cont in range(1,6):
        suma=suma+numero #suma=+suma
        numero=int(input("Dime un número entero mayor que cero: "))
        if(numero<menor):
            menor=numero
        if(numero>mayor):
            mayor=numero
    media=float(suma)/cont

    print("La media vale +"+str(media))
    print("EL MENOR ES "+str(menor))
    print("EL MAYOR ES "+str(mayor))
