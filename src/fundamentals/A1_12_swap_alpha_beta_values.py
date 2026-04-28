print("\nA1 - Ejercicio 12:\n")
print ("""- Suponga que las variables  tienen valores 357 y 59 respectivamente.
            Escriba un programa que intercambie los valores de Alpha y Beta.\n""")

# --- ENTRADA DE DATOS ---
# Definimos los valores directamente en variables, sin usar input() ya que son valores fijos
alpha = 357
beta = 59

swap = 0        # Variable temporal para intercambiar los valores de Alpha y Beta

print("============================================")
print("VALORES ORIGINALES")
print("============================================")
print(f"El valor de alpha: {alpha}")
print(f"El valor de beta: {beta}")
# --- PROCESO ---
# Intercambio de numero de Alpha y Beta usando la variable temporal swap

swap = alpha    # Guardamos el valor de Alpha en la variable temporal swap

alpha = beta    # Asignamos el valor de Beta a Alpha

beta = swap     # # beta toma el valor original de alpha

# --- SALIDA DE DATOS ---
print("\n============================================")
print(f"INTERCAMBIO DE VALORES DE ALPHA Y BETA")
print("============================================\n")
print(f"El nuevo valor de Alpha : {alpha}")
print(f"El nuevo valor de Beta: {beta}")
print("\n")