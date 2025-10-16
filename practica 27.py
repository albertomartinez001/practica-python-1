print("Primeros 10 términos de la serie de Fibonacci:")

a, b = 0, 1
print(a, b, end=" ")

for i in range(2, 10):
    c = a + b
    print(c, end=" ")
    a, b = b, c