

n = int(input("Ingresa el número de términos que deseas mostrar: "))

suma = 0
print("Serie:", end=" ")

for i in range(1, n + 1):
    suma += i
    print(suma, end=", ")
