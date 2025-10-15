print("Ingresa números. El programa terminará cuando ingreses 0.")

while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        print("Número 0 detectado. ¡Programa finalizado!")
        break
    print("Ingresaste:", numero)
