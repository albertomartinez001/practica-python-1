print("Números naturales y sus cuadrados:")
print("Número\tCuadrado")
print("-" * 15)

contador = 1

while contador <= 10:
    cuadrado = contador ** 2
    print(f"{contador}\t{cuadrado}")
    contador += 1