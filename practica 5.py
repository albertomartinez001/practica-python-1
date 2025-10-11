#escribe un programa que determine si una lettra ingresada por el usuairo es vocal o consonate 
letra = input("Ingresa una letra: ").lower()

#inge investigue esta funcion para facilitar el codigo y el manejo de caracteres 
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, ingresa solo una letra válida.")
elif letra in "aeiou":
    print("La letra es una vocal.")
else:
    print("La letra es una consonante.")
