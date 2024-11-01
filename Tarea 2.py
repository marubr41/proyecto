 # Solicitar el número de exámenes
num_examenes = int(input("Ingrese la cantidad de exámenes realizados: "))

# Inicializar variables
suma_notas = 0

# Recoger las notas de los exámenes
for i in range(num_examenes):
    nota = int(input(f"Ingrese la nota del examen {i+1}: "))
    suma_notas += nota

# Calcular el promedio
promedio = suma_notas / num_examenes

# Mostrar la nota final
print(f"La nota final es: {promedio:.2f}")

# Determinar si aprobó, va a ampliación o reprobó
if promedio >= 70:
    print("El estudiante ha aprobado.")
elif 60 <= promedio < 70:
    print("El estudiante debe ir a ampliación.")
else:
    print("El estudiante ha reprobado.")