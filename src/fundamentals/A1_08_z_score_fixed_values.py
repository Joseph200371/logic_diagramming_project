print("\nA1 - Ejercicio 8:\n")

print ("""
La formula de la desviación estándar normal Z, usada en aplicaciones de estadística es Z=(X - m)/s,
    donde m es el valor medio y s es la desviación estándar.
    Usando esta formula, escriba un programa que calcule 
    y despliegue el valor de la desviación estándar normal cuando X = 85,3m = 80 y s = 4
    \n""")

# --- ENTRADA DE DATOS ---
# Se asigan los valores necesarios para calcular la desviación estándar normal Z
# Son valores fijos, no se ingresan por teclado
valor_X = 85.3
valor_medio_m = 80
valor_desviacion_estandar_s = 4

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