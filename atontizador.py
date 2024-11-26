#Guardamos una palabra y la deletreamos
def atontizador():
    palabra=raw_input("Dime una palabra con muchas vocales: ")
    longitud=len(palabra)#Lee el número de letras de la palabra
    for letra in palabra:
        if(letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U'):
            print('U')
        else:
            print(letra)
    print(palabra)
            
atontizador()
