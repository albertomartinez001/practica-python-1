
n = int(input("Ingrese un numero entero positivo: "))

if n <= 0:
    print("Error: El numero debe ser positivo.")
else:
    
    suma = 0
    for i in range(1, n + 1):
        if i % 2 == 0: 
            suma += i   

    print(f"La suma de todos los numeros pares desde 1 hasta {n} es: {suma}")