print("Ingresa números positivos y se irán sumando. Si ingresas un número negativo, el programa se detendrá.")

suma = 0 

while True:
    numero = int(input("Ingresa un número: "))

    if numero < 0:
        print("Número negativo detectado. ¡Programa finalizado!")
        break 

    suma += numero  
    print("La suma actual es:", suma)
