print("\nA1 - Ejercicio 5:\n")
print ("Cálculo de resistencia total en serie.\n")

print ("""
Suponga que debe escribir un programa para calcular la resistencia total de un circuito en serie.
    En tal circuito, la resistencia total es la suma de todos los valores individuales de las resistencias.
    Suponer que el circuito, consiste en una cantidad de 2 resistores de 56 ohmios, 4 de 33 ohmios y 1 de 15 ohmios.
       Responda las siguientes preguntas:
        a) Cuantas salidas requiere este problema de programación.
        b) Cuantos datos de entrada tiene el problema.\n""")

# Mostramos un título
print("CÁLCULO DE RESISTENCIA TOTAL EN SERIE\n")

# ================================
# ENTRADA DE DATOS
# ================================

# Pedimos la cantidad de resistores de 56 ohmios
cantidad_56 = int(input("Ingrese la cantidad de resistores de 56 ohmios: "))

# Pedimos el valor del resistor (aunque ya lo sabemos, lo usamos para practicar input)
valor_56 = 56.00                # Valor fijo para resistores de 56 ohmios

# Pedimos la cantidad de resistores de 33 ohmios
cantidad_33 = int(input("\nIngrese la cantidad de resistores de 33 ohmios: "))

# Pedimos el valor del resistor
valor_33 = 33.00                # Valor fijo para resistores de 33 ohmios

# Pedimos la cantidad de resistores de 15 ohmios
cantidad_15 = int(input("\nIngrese la cantidad de resistores de 15 ohmios: "))

# Pedimos el valor del resistor
valor_15 = 15.00                # Valor fijo para resistores de 15 ohmios


# ================================
# PROCESO
# ================================

# Calculamos resistencias parciales
resistencia_56 = cantidad_56 * valor_56
resistencia_33 = cantidad_33 * valor_33
resistencia_15 = cantidad_15 * valor_15

# Calculamos la resistencia total
resistencia_total = resistencia_56 + resistencia_33 + resistencia_15


# ================================
# SALIDA DE DATOS
# ================================
print("\n==============================")
print("RESULTADOS DEL CIRCUITO")
print("==============================\n")
# --- Cantidad de resistores (56, 33, 15) ohmios --- 
print(f"Cantidad de resistores 56 Ohmios : {cantidad_56:.0f} Ω")
print(f"Cantidad de resistores 33 Ohmios : {cantidad_33:.0f} Ω")
print(f"Cantidad de resistores 15 Ohmios : {cantidad_15:.0f} Ω")

# --- Suma de resistencia ---
print(f"\nResistencia total               : {resistencia_total:.2f} Ω")
print("\n==============================")
print("GRACIAS POR USAR EL PROGRAMA")
print("\n")