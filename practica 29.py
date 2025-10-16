numero_ingresado = int(input("INGRESE UN NUMERO Y IMPRIMIRA TODOS SUS DIVISORES: "))


if numero_ingresado==0:
    print("EL 0 NO ESTA PERMITIDO....")
else:
    for numero in range(1, numero_ingresado+1):
        if numero_ingresado%numero==0:
            print("EL NUMERO: ",numero, "ES DIVISOR DEL:",numero_ingresado)
        