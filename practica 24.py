
numero = int(input("Ingrese un número entero no negativo: "))

if numero < 0:
    print("Error: El factorial no está definido para números negativos.")
else:
    
    factorial = 1
    
    for i in range(1, numero + 1):
        factorial *= i  
    
    print(f"El factorial de {numero} es: {factorial}")