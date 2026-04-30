print("\nA2 - Ejercicio 2:\n")
print ("""- Se conocen dos números distintos:
Calcular la superficie de un cuadrado, suponiendo como lado del mismo al mayor de los números dados 
    y la superficie de un círculo suponiendo como radio del mismo al menor de los números dados.
    Si los números son iguales emitir un mensaje de error.\n""")

# --- ENTRADA DE DATOS ---
# Valor fijo de pi
pi = 3.14

numero_1 = float(input("- Ingrese el primer número: "))

numero_2 = float(input("- Ingrese el segundo número: "))

# --- VALIDACIÓN Y PROCESO ---
if numero_1 == numero_2:               # Se evalua si son iguales
    print("\nError: los números son iguales. Intente con valores distintos.\n")
else:
    # Determinar mayor y menor
    if  numero_2 > numero_1:           # Se evalua si el numero_2 es mayor al numero_1
        num_mayor = numero_2
        num_menor = numero_1
    else:                              # Se evalua si el numero_1 es mayor al numero_2
        num_mayor = numero_1
        num_menor = numero_2

# Cálculos
# Se cálcula las superficie para Cuadrado y circulo
superficie_circulo = pi * (num_menor ** 2)
superficie_cuadrado = num_mayor ** 2

# --- SALIDA DE DATOS ---
print("\n==================================================")
print("RESULTADOS")
print("==================================================")
print(f"Lado del cuadrado (mayor): {num_mayor}")
print(f"Radio del círculo (menor): {num_menor}")
print("--------------------------------------------------")
print(f"Superficie del cuadrado : {superficie_cuadrado:.2f}")
print(f"Superficie del círculo  : {superficie_circulo:.2f}")
print("==================================================\n")