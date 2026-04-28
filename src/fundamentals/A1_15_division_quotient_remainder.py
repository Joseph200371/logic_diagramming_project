print("\nA1 - Ejercicio 14:\n")
print ("""- Dado dos números enteros A y B, 
            calcule el cociente de A dividido en B, y el resto de A dividido en B.\n""")

# --- ENTRADA DE DATOS ---
numero_a = int(input("- Ingrese el numero A: "))
numero_b = int(input("\n- Ingrese el numero B: "))

# --- PROCESO ---
cociente_a = numero_a // numero_b             # Cocientes de A dividido en B
restos_a = numero_a % numero_b               # Restos de A dividido en B

# --- SALIDA DE DATOS ---
print("\n==================================================")
print("CÁLCULO DE COCIENTE Y RESTO DE A DIVIDIDO EN B")
# Mostramos el resultado con 2 decimales
print("==================================================")
print(f"Número A: {numero_a} y Número B: {numero_b} => Cociente: {cociente_a} y Resto: {restos_a}")
print("==================================================\n")
print("\n")