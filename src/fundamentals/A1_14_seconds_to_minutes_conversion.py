print("\nA1 - Ejercicio 14:\n")
print ("""- Dado un número de segundos haga la conversión en minutos y segundos.\n""")

# --- ENTRADA DE DATOS ---
segundos_por_minuto = 60                                             # Valor fijo de conversión de segundos a minutos
print("--- Segundos a minutos y segundos ---")
segundos_ingresados = int(input("- Ingrese segundos: "))

# --- PROCESO ---
resultado_minutos = int(segundos_ingresados / segundos_por_minuto)
resto_segundos = segundos_ingresados % segundos_por_minuto           # Restos de segundos que no completan un minuto

# --- SALIDA DE DATOS ---
print("\n============================================")
print("CÁLCULO DE SEGUNDOS A MINUTOS Y SEGUNDOS")
# Mostramos el resultado con 2 decimales
print("============================================")
print(f"{segundos_ingresados} Segundos = {resultado_minutos} Minutos y {resto_segundos} Segundos")
print("============================================\n")
print("\n")