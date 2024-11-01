# Solicitar al usuario un número
numero = int(input("Ingrese un número: "))

# Verificar si el número es mayor o igual a 0
if numero < 0:
    print("Error: El número ingresado es menor que 0.")
else:
    # Verificar si el número es mayor a 100
    if numero > 100:
        print("Resultado:", numero - 100)
    else:
        print("Resultado:", numero)
        