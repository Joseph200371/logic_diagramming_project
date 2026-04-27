print("\nA1 - Ejercicio 3:\n")
print ("""
Un negocio de deportes hace un 25% de descuento en pelotas de fútbol y de béisbol.
    Se requiere escribir un programa que le permita a un empleado ingresar los precios originales de las pelotas.
    El programa deberá usar estas entradas de datos para calcular el precio rebajado.
    La salida del programa deberá mostrar, en líneas separadas, el precio original y el precio con descuento.\n""")

# Definimos el porcentaje de descuento (25% = 0.25)
descuento = 0.25

# Pedimos al usuario que ingrese el precio original
# input() siempre devuelve texto, por eso lo convertimos a número con float()
precio_futbol = float(input("Ingrese el precio de la pelota de fútbol: "))
precio_beisbol = float(input("Ingrese el precio de la pelota de béisbol: "))
print("\n")     # Salto de línea para mejorar la legibilidad

# Calculamos los precios totales (SIN DESCUENTOS)
precios_totales = precio_futbol + precio_beisbol

# Calculamos los precios finales
precio_futbol_desc = precio_futbol * (1 - descuento)
precio_beisbol_desc = precio_beisbol * (1 - descuento)

# Calculamos los precios totales (CON DESCUENTOS)
precio_final = precio_futbol_desc + precio_beisbol_desc

# Mostramos los resultados
print("--------------------------------------------------------------")
print("TOTAL SIN DESCUENTOS $ ", precios_totales)
print("--------------------------------------------------------------\n")
# --- Pelota de fútbol ---
print("Pelota de fútbol: $", precio_futbol)
print("Porcentaje de Descuento: ", descuento * 100, "%")
print("Descuento: $ ", precio_futbol * descuento)
print("Precio con descuento: $ ", precio_futbol_desc)
# --- pelota de béisbol
print("\nPelota de béisbol: $", precio_beisbol)
print("Descuento: ", descuento * 100, "%")
print("Descuento: $ ", precio_beisbol * descuento)
print("Precio con descuento: $ ", precio_beisbol_desc)
print("\n--------------------------------------------------------------")
print("TOTAL", precio_final)
print("--------------------------------------------------------------")

input("\nPresione Enter para continuar...")  # pausamos la ejecución

print(f"\nPelota de Fútbol -> Precio Original: $ {precio_futbol} | Descuento: $ {precio_futbol * descuento} | Precio con Descuento: $ {precio_futbol_desc}")
print(f"\nPelota de Béisbol -> Precio Original: $ {precio_beisbol} | Descuento: $ {precio_beisbol * descuento} | Precio con Descuento: $ {precio_beisbol_desc} \n")