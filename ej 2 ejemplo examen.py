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
            # Solicitar al usuario un número
            numero = int(input("Introduce un número entero no negativo para calcular su factorial: "))
            
            # Comprobar si el número es negativo
            if numero < 0:
                print("Error: El número no puede ser negativo. Inténtalo de nuevo.")
            else:
                # Calcular el factorial utilizando ambas técnicas
                print(f"El factorial de {numero} utilizando 'for' es: {factorial_for(numero)})
                print(f"El factorial de {numero} utilizando 'while' es: {factorial_while(numero)})
                break
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

# Llamada a la función principal para ejecutar el programa
calcular_factorial()
