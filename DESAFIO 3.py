# EJERCICIO 7 - DESAFIO 3
# clientes = ["Sofia", "Andres", "Camilo"]
# print(clientes)
# productos = ["Celular", "Portatil", "Tablet"]
# print(productos)
# # punto1=input("La lista de cleintes tiene tres nombres, si crees que se encuentra Camilo ingresa 'SI' de lo contrario ingresa 'NO': ")
# #Punto 1
# # if punto1=="SI":
# #     print("Camilo está en la lista de clientes. Se modificará y se agragará el nombre Valeria...")
# #     clientes[2]="Valeria"
# #     print(clientes)
# # else:
# #     print(f"Camilo no está en la lista.")

# Punto2=input(f"En la lista de productos, crees que se encuentra 'Tablet'?(Contesta 'SI' o 'NO' todo en mayusculas): ")
# if punto2=="SI":
#     print(f"Tablet está en la lista de productos. Agregando Impresora...")
#     productos.append("Impresora")
#     print(productos)
# else:
#     print("Tablet no está en la lista.")

# Punto3=input("Andres esta en la lista, deseas eliminarlo?: ")
# if Punto3=="SI":
#     print(f"Andres está en la lista de clientes. Eliminándolo...")
#     clientes.remove("Andres")
#     print(clientes)
# else:
#     print(f"Andres no fue eliminado.")

# Punto 4 
# if len(productos) > 3:
#     print(f"Hay más de 3 productos. Eliminando el primero...")
#     productos.pop(0)
#     print(productos)
# else:
#     print(f"No hay más de 3 productos.")

# Punto5=input("Deseas cambiar 'Celular' a 'smartwatch'?: ")
#  if Punto5=="SI":
#     print(f"Celular ya no está en la lista. Agregando smartwatch...")
#     productos.append(f"smartwatch")
# else:
#     print(f"Celular sigue en la lista.")

# Punto 6
# nuevo_cliente = None
# if "Valeria" in clientes:
#     print(f"Valeria está en la lista de clientes. Creando tupla...")
#     nuevo_cliente = ("Valeria", "Impresora")
# else:
#     print(f"Valeria no está en la lista.")

# Punto 7
# destacados = clientes[:2]
# print(f"Destacados:{destacados}")  

# Punto 8
# inventario = productos[-2:]
# print(f"Inventario:{ inventario}")  

# Punto 9
# smartwatch_en_inventario = input("¿Está el smartwatch en el inventario? (sí/no): ").strip().lower()
# if smartwatch_en_inventario == "sí":
#     productos.append("Accesorios")
# else:
#     print("No se añadió Accesorios")

# Punto 10
# if "Sofia" in destacados:
#     ficha_cliente = {
#         "Nombre": "Sofia",
#         "Producto": "Portatil",
#         "Activo": True
#     }
# else:
#     print("Sofia no está en destacados")

# Punto 11
# if 'ficha_cliente' in locals():
#     ficha_cliente["Frecuencia"] = "mensual"
#     print(f"Se agregó una nueva clave:{ficha_cliente}")
# else:
#     print("No existe este diccionario")

# Punto 12
# if "Tablet" not in productos:
#     productos.append("Tablet")
#     print(productos)
# else:
#     print("Tablet si está en la lista")

# Punto 13
# if "Valeria" not in clientes:
#     clientes.append("Valeria")

# Punto 14
# print("Listas:")
# print(f"Clientes:{clientes}")
# print(f"Productos:{productos}")
# print(f"Destacados:{destacados}")
# print(f"Inventario:{inventario}")

# if 'ficha_cliente' in locals():
#     print(f"Diccionario ficha_cliente:{ficha_cliente}")