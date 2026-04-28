print("\nA1 - Ejercicio 13:\n")
print ("""- Desarrolle un programa que transforme a centímetros un valor ingresado en pulgadas (1 pulgada = 2.54 cm).
    \n""")

# --- ENTRADA DE DATOS ---
factor_conversion = 2.54                 # Valor fijo de conversión de pulgadas a centrímetros
print("--- Pulgadas a Centímetros ---")
# El valor ingresado es tipo float para permitir decimales, ya que las pulgadas pueden ser fraccionarios
valor_pulgadas = float(input("- Ingrese pulgadas: "))

# --- PROCESO ---
# Multiplicamos centímetros (factor_conversion) por pulgadas (valor_pulgadas)
resultado_cm = factor_conversion * valor_pulgadas

# --- SALIDA DE DATOS ---
print("\n============================================")
print("CÁLCULO DE PULGADAS A CENTRÍMETROS")
# Mostramos el resultado con 2 decimales
print("============================================")
print(f"{valor_pulgadas} pulgadas = {resultado_cm:.2f} cm")
print("============================================\n")
print("\n")