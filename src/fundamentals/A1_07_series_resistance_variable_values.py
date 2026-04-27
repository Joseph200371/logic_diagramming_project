print("\nA1 - Ejercicio 7:\n")

print ("""
Suponga que debe escribir un programa para calcular la resistencia total de un circuito en serie.
    En tal circuito, la resistencia total es la suma de todos los valores individuales de las resistencias.
    Deberá ingresar las cantidades de resistencia y de ohmios para cada resistencia.
    Suponer que el circuito, consiste en una cantidad de XX resistores de ZZ ohmios, XX de ZZ ohmios y XX de ZZ ohmios.
    \n""")

# --- ENTRADA DE DATOS ---
# Pedimos la cantidad de resistores para cada grupo de resistencias
cantidad_resistores_1 = int(input("\n - Ingrese la cantidad de resistores para la primera resistencia: "))
cantidad_resistores_2 = int(input("\n - Ingrese la cantidad de resistores para la segunda resistencia: "))
cantidad_resistores_3 = int(input("\n - Ingrese la cantidad de resistores para la tercera resistencia: "))

# Pedimos el valor de ohmios para cada grupo de resistencias
ohmios_valor_1 = int(input("\n - Ingrese el valor de ohmios para la primera resistencia: "))
ohmios_valor_2 = int(input("\n - Ingrese el valor de ohmios para la segunda resistencia: "))
ohmios_valor_3 = int(input("\n -Ingrese el valor de ohmios para la tercera resistencia: "))

# --- PROCESO ---
# Calculos de resistencias parciales
resistencia_1 = cantidad_resistores_1 * ohmios_valor_1
resistencia_2 = cantidad_resistores_2 * ohmios_valor_2
resistencia_3 = cantidad_resistores_3 * ohmios_valor_3

# Suma de resistencias totales en series
resistencia_total = resistencia_1 + resistencia_2 + resistencia_3

# --- SALIDA DE DATOS ---
print("\n==================================================================")
print("RESULTADOS DEL CIRCUITO")
print("====================================================================\n")
# --- Cantidad de resistencia ---
print(f"Cantidad de resistores (grupo 1): {cantidad_resistores_1:.0f}")
print(f"Cantidad de resistores (grupo 2): {cantidad_resistores_2:.0f}")
print(f"Cantidad de resistores (grupo 3): {cantidad_resistores_3:.0f}")

# --- Valor de ohmios para cada resistencias ---
print(f"\nEl valor de ohmios para la primera resistencia: {ohmios_valor_1 :.0f} Ω")
print(f"El valor de ohmios para la segunda resistencia: {ohmios_valor_2:.0f} Ω")
print(f"El valor de ohmios para la tercera resistencia: {ohmios_valor_3:.0f} Ω")

# --- Las resistencias totales en series ---
print(f"\nResistencia grupo 1: {resistencia_1} Ω")
print(f"Resistencia grupo 2: {resistencia_2} Ω")
print(f"Resistencia grupo 3: {resistencia_3} Ω")

# --- Resultado de la suma de resistencias ---
print(f"\nLa resistencia total del circuito en serie es: {resistencia_total} Ω")
print("\n===================================================================")
print("GRACIAS POR USAR EL PROGRAMA")
print("===================================================================")
print("\n")