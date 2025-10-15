numero = int(input("Ingresa un número y se mostrará la secuencia de Fibonacci hasta ese valor: "))

a, b = 0, 1 

print("Secuencia de Fibonacci:")

while a <= numero:
    print(a)
    a, b = b, a + b  
