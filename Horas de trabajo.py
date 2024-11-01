#Solicitar las horas trabajadas y el coste por hora
horas_trabajadas = input("Ingrese el número de horas trabajadas: ")
coste_por_hora = input("Ingrese el coste por hora: ")

# Convertir a flotante y asumir valores numéricos válidos
es_valido = horas_trabajadas.replace('.', '', 1).isdigit() and coste_por_hora.replace('.', '', 1).isdigit()

# Usar booleano para forzar que las entradas solo se procesen si son válidas
horas_trabajadas = float(horas_trabajadas) if es_valido else 0.0
coste_por_hora = float(coste_por_hora) if es_valido else 0.0

# Calcular la paga
paga = horas_trabajadas * coste_por_hora
