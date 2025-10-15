numero = int(input("Ingresa un número: "))

if numero % 5 == 0 and numero % 7 == 0:
    print(f"El número {numero} es múltiplo de 5 y de 7.")
else:
    print(f"El número {numero} NO es múltiplo de 5 y de 7.")
    