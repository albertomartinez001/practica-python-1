punteo = int(input("Ingrese la calificación (0-100): "))

if punteo > 100 or punteo < 0:
    print("¡La calificación NO es válida!")
elif punteo >= 90 and punteo <= 100:
    print("Aprobado con A")
elif punteo >= 80 and punteo <= 89:
    print("Aprobado con B")
elif punteo >= 70 and punteo <= 79:
    print("Aprobado con C")
elif punteo >= 60 and punteo <= 69:
    print("Aprobado con D")
else:
    print("Reprobado con F")