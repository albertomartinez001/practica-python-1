print("Ingresa números y se irán sumando. El programa se detendrá cuando la suma sea mayor a 100.")

suma = 0

while True:
    numero = int(input("Ingresa un número: "))
    suma += numero  

    print("La suma actual es:", suma)

    if suma > 100:
        print("La suma total superó 100. ¡Programa finalizado!")
        break
