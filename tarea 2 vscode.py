#Tarea ded Eliana Bustamante Rivera 
numexamenes = int(input("Ingrese la cantidad de exámenes realizados: "))

sumanotas = 0

for i in range(numexamenes):
    nota = int(input(f"Ingrese la nota del examen {i+1}: "))
    sumanotas += nota

promedio = sumanotas / numexamenes

print(f"La nota final es: {promedio:.2f}")

if promedio >= 70:
    print("El estudiante ha aprobado.")
elif 60 <= promedio < 70:
    print("El estudiante debe ir a ampliación.")
else:
    print("El estudiante ha reprobado.")