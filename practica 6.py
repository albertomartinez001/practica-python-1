numero = int(input("Ingresa un numero para saber si es primo o no: "))

if numero<2:
    print("El numero no puede ser primo")
else:
    sera_primo= True

    
    for i in range (2, int(numero**0.5)+1):
        if numero % i ==0:
            sera_primo= False
            break
    

    if sera_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")