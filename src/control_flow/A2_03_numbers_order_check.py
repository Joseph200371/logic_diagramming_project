print("\nA2 - Ejercicio 3:\n")
print ("""- Lea 3 números enteros y emita un mensaje que indique si están o no en orden numérico.\n""")

# --- ENTRADA DE DATOS ---
numero_1 = int(input("- Ingrese el primer número: "))
numero_2 = int(input("\n- Ingrese el segundo número: "))
numero_3 = int(input("\n- Ingrese el tercero número: "))

# --- VALIDACIÓN Y PROCESO ---
if numero_1 == numero_2 == numero_3:
   print(f"\nLos números son iguales: {numero_1, numero_2, numero_3}\n")
else:
    if numero_1 < numero_2 < numero_3:
        print(f"\nLos números están en orden creciente: {numero_1, numero_2, numero_3}\n")
    elif numero_1 > numero_2 > numero_3:
        print(f"\nLos números están en orden decreciente: {numero_1, numero_2, numero_3}\n")
    else:
        print(f"\nLos números no están en orden: {numero_1, numero_2, numero_3}\n")