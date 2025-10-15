numero = int(input("Ingresa un número: "))

contador = 0

print(f"Números pares hasta {numero}:")


while contador <= numero:
    
    if contador % 2 == 0:
        print(contador)
    
    
    contador += 1