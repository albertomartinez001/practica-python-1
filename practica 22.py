numero = int(input("Ingrese un numero y le daremos la tabla del 1 al 10 de ese mismo numero: "))

for i in range(1, 11, 1):
    resultado=i*numero
    print(numero, " X ", i," = ",resultado)