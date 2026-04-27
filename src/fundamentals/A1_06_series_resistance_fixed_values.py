print("\nA1 - Ejercicio 6:\n")

print ("""
Suponga que debe escribir un programa para calcular la resistencia total de un circuito en serie.
    En tal circuito, la resistencia total es la suma de todos los valores individuales de las resistencias.
    Deberá ingresar las cantidades de ohmios para cada resistencia.
    Suponer que el circuito, consiste en una cantidad de 2 resistores de XX ohmios, 4 de XX ohmios y 1 de XX ohmios.
    \n""")

# --- ENTRADA DE DATOS ---
# Pedimos el valor de cada resistor para los grupos de 2, 4 y 1 resistores
valor_resistor_1 = int(input("Valor de cada resistor (grupo de 2): "))
valor_resistor_2 = int(input("Valor de cada resistor (grupo de 4): "))
valor_resistor_3 = int(input("Valor de cada resistor (grupo de 1): "))

# Cantidades fijas de resistores 
cantidad_resistores_1 = 2      
cantidad_resistores_2 = 4
cantidad_resistores_3 = 1

# --- PROCESO ---
# Calculos de resistencias parciales
resistencia_1 = cantidad_resistores_1 * valor_resistor_1
resistencia_2 = cantidad_resistores_2 * valor_resistor_2
resistencia_3 = cantidad_resistores_3 * valor_resistor_3

# Suma total en serie
resistencia_total = resistencia_1 + resistencia_2 + resistencia_3

# --- SALIDA DE DATOS ---
print("\n==================================================================")
print("RESULTADOS DEL CIRCUITO")
print("====================================================================\n")
# --- Cantidad de resistencia de los grupos (2, 4 y 1) ---
print(f"Grupo de 2 resistores                          : {resistencia_1:.0f}")
print(f"Grupo de 4 resistores                          : {resistencia_2:.0f}")
print(f"Grupo de 1 resistor                            : {resistencia_3:.0f}")

# --- Resultado de la suma de resistencias ---
print(f"\nLa resistencia total del circuito en serie es: {resistencia_total} Ω")
print("\n===================================================================")
print("GRACIAS POR USAR EL PROGRAMA")
print("===================================================================")
print("\n")