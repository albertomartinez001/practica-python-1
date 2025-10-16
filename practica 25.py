print("Números primos del 1 al 50:")

for numero in range(1, 51):
    
    if numero > 1:
        es_primo = True
        
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        
        if es_primo:
            print(numero, end=" ")