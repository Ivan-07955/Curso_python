def factorial_for(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_while(n):
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += 1
    return resultado

def calcular_factorial():
    while True:
        try:
            # Solicitar al usuario un n�mero
            numero = int(input("Introduce un n�mero entero no negativo para calcular su factorial: "))
            
            # Comprobar si el n�mero es negativo
            if numero < 0:
                print("Error: El n�mero no puede ser negativo. Int�ntalo de nuevo.")
            else:
                # Calcular el factorial utilizando ambas t�cnicas
                print(f"El factorial de {numero} utilizando 'for' es: {factorial_for(numero)})
                print(f"El factorial de {numero} utilizando 'while' es: {factorial_while(numero)})
                break
        except ValueError:
            print("Error: Por favor, introduce un n�mero entero v�lido.")

# Llamada a la funci�n principal para ejecutar el programa
calcular_factorial()
