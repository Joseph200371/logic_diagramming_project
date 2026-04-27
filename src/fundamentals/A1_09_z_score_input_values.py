print("\nA1 - Ejercicio 9:\n")
print ("""
La formula de la desviación estándar normal Z, usada en aplicaciones de estadística es Z=(X - m)/s, 
    donde m es el valor medio y s es la desviación estándar. 
    Usando esta formula, escriba un programa que calcule y despliegue el valor de la desviación estándar normal.
    Ingresar los valores necesarios para poder calcular la desviación estándar.
    \n""")

# --- ENTRADA DE DATOS ---
# Se asigan los valores necesarios para calcular la desviación estándar normal Z
valor_X = float(input(" - Ingrese el valor de X : "))
valor_medio_m = float(input("\n - Ingrese el valor medio (m) : "))
valor_desviacion_estandar_s = float(input("\n - Ingrese el valor de la desviación estándar (s) : "))

# --- PROCESO ---
# Cálculo de Z: (X - m) / s
desviacion_estandar_normal_Z = (valor_X - valor_medio_m) / valor_desviacion_estandar_s

# --- SALIDA DE DATOS ---
print("\n==================================================================")
print("RESULTADOS DESVIACIÓN ESTÁNDAR NORMAL Z")
print("====================================================================\n")
print("Los valores de entrada para el cálculo de la desviación estándar normal Z son: \n")
print(f"X = {valor_X}")
print(f"Media (m) = {valor_medio_m}")
print(f"Desviación estándar (s) = {valor_desviacion_estandar_s}")
# Se muestra el resultado de la desviación estándar normal Z con dos decimales de precisión
print(f"\nEl resultado de la desviación estándar normal Z es: {desviacion_estandar_normal_Z:.2f}")
print("\n==================================================================")