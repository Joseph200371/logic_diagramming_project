print("\nA2 - Ejercicio 5:\n")
print ("""
- Hacer un programa que permita ingresar una fecha para luego mostrarla. 
    Se debe validar que la fecha ingresada sea anterior a la fecha actual 
    y en caso de que no cumplan con dicha condición se deberá mostrar un mensaje de error.\n""")

# --- ENTRADA DE DATOS ---
dia_actual = 30
mes_actual = 4
anio_actual = 2026

print("\nLa fecha en formato DIA - MES - AÑOS (ej: 12 5 2026)\n")
dia_ingresada  = int(input("- Ingrese el dia: "))
mes_ingresada  = int(input("- Ingrese el mes: "))
anio_ingresada  = int(input("- Ingrese el año: "))

# --- VALIDACIÓN Y PROCESO ---
# Si fecha ingresada == fecha actual → Solo informar
if (anio_ingresada == anio_actual) and (mes_ingresada == mes_actual) and (dia_ingresada == dia_actual):
    print("\nNo es anterior a la fecha actual, Son iguales")
else:
    if (anio_ingresada < anio_actual):                                            # Si año ingresado < año actual → ✔️ anterior
        print("\nLa fecha es anterior")
    elif (anio_ingresada > anio_actual):                                          # Si año ingresado > año actual → ❌ error
        print("\nERROR: La fecha ingresada no es valido")
    else:
        if (mes_ingresada < mes_actual):                                          # Si mes ingresado < mes actual → ✔️ anterior
            print("\nLa fecha es anterior")
        elif (mes_ingresada > mes_actual):                                        # Si mes ingresado > mes actual → ❌ error
            print("\nERROR: La fecha ingresada no es valido")
        else:
            if (dia_ingresada < dia_actual):                                      # Si día ingresado < día actual → ✔️ anterior
                print("\nLa fecha es anterior")
            elif (dia_ingresada >= dia_actual):                                   # Si día ingresado >= día actual → ❌ error
                print("ERROR: La fecha ingresada no es valido")

print("\n==================================================\n")
print(f"Fecha actual es     : {dia_actual} / {mes_actual} / {anio_actual}\n")
print(f"Fecha Ingresada es  : {dia_ingresada} / {mes_ingresada} / {anio_ingresada}")