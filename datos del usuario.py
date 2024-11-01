 #Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
estatura = float(input("Ingrese su estatura en metros (ejemplo: 1.75): "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Calcular el Índice de Masa Corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el mensaje con el IMC
print("Hola " + nombre + ", tu Índice de Masa Corporal (IMC) es " + str(round(imc, 2)))