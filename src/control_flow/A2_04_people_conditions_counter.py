print("\nA2 - Ejercicio 4:\n")
print ("""- Se ingresa nombre, sexo y edad de 3 personas.
            Se pide averiguar cuántas mujeres tienen entre 20 y 30 años y cuantos hombres son menores a 37 años.\n""")

# --- ENTRADA DE DATOS ---
cantidad_male_menores_37 = 0
cantidad_female_menores_20_30 = 0

print("Información de la primera persona:")
nombre_1 = input("\n- Ingrese su nombre: ")
sexo_1 = input("- Ingrese su sexo << Masculino = M >> O << Femenino = F >> : ")
edad_1 = int(input("- Ingrese su edad: "))

print("\nInformación de la segunda persona:")
nombre_2 = input("\n- Ingrese su nombre: ")
sexo_2 = input("- Ingrese su sexo << Masculino = M >> O << Femenino = F >> : ")
edad_2 = int(input("- Ingrese su edad: "))

print("Información de la tercera persona:")
nombre_3 = input("\n- Ingrese su nombre: ")
sexo_3 = input("- Ingrese su sexo << Masculino = M >> O << Femenino = F >> : ")
edad_3 = int(input("- Ingrese su edad: "))

# --- VALIDACIÓN Y PROCESO ---
if sexo_1 == "F" and (edad_1 > 20 and edad_1 < 30):
    cantidad_female_menores_20_30 = cantidad_female_menores_20_30 + 1
if sexo_2 == "F" and (edad_2 > 20 and edad_2 < 30):
    cantidad_female_menores_20_30 = cantidad_female_menores_20_30 + 1
if sexo_3 == "F" and (edad_3 > 20 and edad_3 < 30):
    cantidad_female_menores_20_30 = cantidad_female_menores_20_30 + 1
if sexo_1 == "M" and edad_1 < 37:
    cantidad_male_menores_37 = cantidad_male_menores_37 + 1
if sexo_2 == "M" and edad_2 < 37:
    cantidad_male_menores_37 = cantidad_male_menores_37 + 1
if sexo_3 == "M" and edad_3 < 37:
    cantidad_male_menores_37 = cantidad_male_menores_37 + 1


# --- SALIDA DE DATOS ---
print("\n==================================================")
print("RESULTADOS")
print("==================================================")
print(f"Mujeres entre 20 y 30 años : {cantidad_female_menores_20_30}")
print(f"Hombres menores a 37 años  : {cantidad_male_menores_37}")
print("==================================================\n")