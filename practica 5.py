
letra = input("Ingresa una letra: ").lower()

 
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, ingresa solo una letra válida.")
elif letra in "aeiou":
    print("La letra es una vocal.")
else:
    print("La letra es una consonante.")
