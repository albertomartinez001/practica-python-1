precio= int(input("INgrese el precio del producto: "))
print("EJemplo de como ingresar el descuento:(50) solo ingrese la cantidad de descuento")
descuento = int(input("Ingrese el porcentaje de descuento: "))

descuento_transformado= descuento/100

descuento_total= precio*descuento_transformado

cantidad_final= precio-descuento_total

print("su descuento es: ", descuento_total, "por lo que debera pagar nada mas: ", cantidad_final)
