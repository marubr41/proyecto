def calcular_paga(horas_trabajadas, coste_por_hora):
    paga = horas_trabajadas * coste_por_hora
    return paga

# Entrada de datos
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
coste_por_hora = float(input("Ingrese el coste por hora: "))

# Cálculo y salida
paga = calcular_paga(horas_trabajadas, coste_por_hora)
print(f"La paga correspondiente es: {paga:.2f} unidades monetarias.")