# Almacenar en una lista los siguientes precios, 43, 57, 92, 20, 37, 5, 9, y mostrar en pantalla  el menor y el mayor de los precios.
print(" ") # ESPACIO
print("Alvarez Delgado Yael Ismael: Ejercicio 1   3W")  # Texto que sale en pantalla
print(" ")  # ESPACIO

# lista de los precios
precios = [43, 57, 92, 20, 37, 5, 9]

# Encontrar el menor y el mayor precio
menor_precio = min(precios)
mayor_precio = max(precios)

# Mostrar los resultados
print(f"El menor precio es: {menor_precio}")
print(f"El mayor precio es: {mayor_precio}")

print(" ")
[print(x) for x in precios]



