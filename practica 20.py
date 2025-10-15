print("Cálculo del producto de los primeros 10 números naturales:")

contador = 1
producto = 1  

while contador <= 10:
    print(f"Multiplicando por {contador}")
    producto = producto * contador
    contador += 1

print(f"\nEl producto de los primeros 10 números naturales es: {producto}")