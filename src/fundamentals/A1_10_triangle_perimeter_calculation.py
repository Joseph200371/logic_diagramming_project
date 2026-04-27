print("\nA1 - Ejercicio 10:\n")
print ("""- Dado el valor de los tres lados de un triangulo, calcular el perímetro\n""")

# --- ENTRADA DE DATOS ---
lado_a = float(input("- Ingrese el valor del lado a : "))
lado_b = float(input("\n- Ingrese el valor del lado b : "))
lado_c = float(input("\n- Ingrese el valor del lado c : "))

# --- PROCESO ---
# Se calcula el perímetro sumando los tres lados
perimetro = lado_a + lado_b + lado_c

# --- SALIDA DE DATOS ---
print("\n============================================")
print("CÁLCULO DEL PERÍMETRO DE UN TRIÁNGULO")
print("============================================\n")
# Mostramos el resultado con 2 decimales
print("\n============================================")
print(f"El perímetro del triángulo es: {perimetro:.2f}")
print("============================================\n")
print("\n") 