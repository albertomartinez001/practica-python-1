print("Ejemplo de como se debe ingresar el año: 1999")
año = int(input("Ingrese un año pasa saber si es un año valido: "))

if año>1900 and año <2025:
    print("EL AÑO INGRESADO ES VALIDO POR QUE CUMPLE LA CONDICION")
else:
    print("EL año: ",año," NO ES VALIDO PORQUE NO CUMPLE LA CONDICION")