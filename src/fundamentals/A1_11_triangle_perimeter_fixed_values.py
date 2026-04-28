print("\nA1 - Ejercicio 11:\n")
print ("""- Dado el valor de los tres lados de un triangulo L1 = 10, L2 = 12 y L3 = 8, calcular el perímetro.\n""")

# --- ENTRADA DE DATOS ---
# Definimos los valores directamente en variables, sin usar input() ya que son valores fijos
lado_a = 10.0
lado_b = 12.0
lado_c = 8.0

# --- PROCESO ---
# Se calcula el perímetro sumando los tres lados
perimetro = lado_a + lado_b + lado_c

# --- SALIDA DE DATOS ---
print("\n============================================")
print("CÁLCULO DEL PERÍMETRO DE UN TRIÁNGULO")
print("============================================")
print(f"Lado a (L1): {lado_a:.2f}")
print(f"Lado b (L2): {lado_b:.2f}")
print(f"Lado c (L3): {lado_c:.2f}")
# Mostramos el resultado con 2 decimales
print("============================================")
print(f"El perímetro del triángulo es: {perimetro:.2f}")
print("============================================\n")
print("\n") 