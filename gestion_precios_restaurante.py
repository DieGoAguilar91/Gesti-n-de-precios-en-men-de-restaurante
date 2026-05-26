# Gestión de precios en menú de restaurante
# Autor: Diego Stiven Aguilar González
# Grupo: 213022A_2201
# Programa: Ingeniería en Sistemas - UNAD

# Matriz de productos: [Nombre, Categoría, Precio Base]
productos = [
    ["Hamburguesa", "Plato Fuerte", 15000],
    ["Ensalada", "Entrada", 8000],
    ["Postre de Chocolate", "Postre", 6000],
    ["Sopa de Mariscos", "Entrada", 11000],
    ["Spaghetti Bolonesa", "Plato Fuerte", 12000],
    ["Café", "Bebida", 3000]
]

# Función para calcular el precio final
def calcular_precio_final(producto, categoria_objetivo, umbral):
    nombre, categoria, precio_base = producto
    if categoria == categoria_objetivo and precio_base > umbral:
        precio_final = precio_base * 0.85  # Aplicar 15% descuento
    else:
        precio_final = precio_base         # Mantener precio base
    return nombre, categoria, precio_base, precio_final

# Mostrar resultados
print("Nombre".ljust(20), "Categoría".ljust(15), "Precio Base".ljust(12), "Precio Final")
print("-" * 65)
for item in productos:
    #se eligió "Plato Fuerte" como categoría objetivo porque: es una categoría 
    #común en los menús de restaurante
    nombre, categoria, precio_base, precio_final = calcular_precio_final(item, "Plato Fuerte", 10000)
    print(nombre.ljust(20), categoria.ljust(15), str(precio_base).ljust(12), str(int(precio_final)).ljust(12))
