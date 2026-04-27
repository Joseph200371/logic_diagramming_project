print("\nA1 - Ejercicio 4:\n")
print ("""
Un negocio de deportes hace un descuento en pelotas de fútbol y de béisbol.
    Se requiere escribir un programa que le permita a un empleado ingresar los precios originales de las pelotas y de los descuentos.
    El programa deberá usar estas entradas de datos para calcular el precio rebajado.
    La salida del programa deberá mostrar, en líneas separadas, el precio original y el precio con descuento.\n""")

# ================================
# PELOTA DE FÚTBOL
# ================================

# Pedimos al usuario que ingrese el precio original y el descuento
# input() siempre devuelve texto, por eso lo convertimos a número con float()
precio_futbol = float(input("Ingrese el precio de la pelota de fútbol: "))
descuento_futbol_ingresado = float(input("Ingrese el descuento (%) para la pelota de fútbol: "))

# realizamos los calculo matemetico necesario
descuento_futbol = descuento_futbol_ingresado / 100             # Convertimos el porcentaje a decimal
monto_descuento_futbol = precio_futbol * descuento_futbol       # Calculamos el monto de descuento
precio_final_futbol = precio_futbol - monto_descuento_futbol    # Calculamos el precio final    

# ================================
# PELOTA DE BÉISBOL
# ================================

# Pedimos al usuario que ingrese el precio original
# input() siempre devuelve texto, por eso lo convertimos a número con float()
precio_beisbol = float(input("\nIngrese el precio de la pelota de béisbol: "))
descuento_beisbol_ingresado = float(input("Ingrese el descuento (%) para la pelota de béisbol: "))

# realizamos los calculo matemetico necesario
descuento_beisbol = descuento_beisbol_ingresado / 100                   # Convertimos el porcentaje a decimal
monto_descuento_beisbol = precio_beisbol * descuento_beisbol            # Calculamos el monto de descuento
precio_final_beisbol = precio_beisbol - monto_descuento_beisbol         # Calculamos el precio final 

# --- Suma de ambas pelotas con precio original ---
precios_totales = precio_futbol + precio_beisbol

# --- Suma de ambas pelotas con descuentos ---
precios_totales_desc = precio_final_futbol + precio_final_beisbol

# ================================
# TICKETS
# ================================

print("\n==============================")
print("      TICKET DE COMPRA")
print("==============================")

# --- Precio de ambas pelotas ---
print("------------------------------")
print("TOTAL SIN DESCUENTOS $ ", precios_totales)
print("------------------------------\n")
# --- FÚTBOL ---
print("\nProducto: Pelota de fútbol")
print("------------------------------")
print(f"Precio original : $ {precio_futbol:.2f}")
print(f"Descuento (%)   :   {descuento_futbol_ingresado:.0f}%")
print(f"Ahorro          : $ {monto_descuento_futbol:.2f}")
print(f"Precio final    : $ {precio_final_futbol:.2f}")

# ----- BÉISBOL -----
print("\nProducto: Pelota de béisbol")
print("------------------------------")
print(f"Precio original : $ {precio_beisbol:.2f}")
print(f"Descuento (%)   :   {descuento_beisbol_ingresado:.0f}%")
print(f"Ahorro          : $ {monto_descuento_beisbol:.2f}")
print(f"Precio final    : $ {precio_final_beisbol:.2f}")

# --- Precio de ambas pelotas ---
print("\n------------------------------")
print(f"PRECIO TOTAL    : $ {precios_totales_desc:.2f}")
print("------------------------------")

print("\n==============================")
print("   GRACIAS POR SU COMPRA")
print("==============================")

print ("\n")
