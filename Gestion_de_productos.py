productos = []

def cargar_datos():
    try:
        with open("productos.txt", "r") as file:
            for linea in file:
                nombre, precio, cantidad, descripcion = linea.strip().split(", ")
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad),
                    'descripcion': descripcion
                })
        print("Datos cargados exitosamente.")
    except FileNotFoundError:
        print("Archivo no encontrado, comenzando con inventario vacío.")
    except ValueError:
        print("Error al leer el archivo, verifica el formato de los datos.")

def guardar_datos():
    """Guarda los productos en el archivo productos.txt."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}, {producto['descripcion']}\n")
    print("Datos guardados exitosamente.")
def añadir_producto():
    """Permite añadir un nuevo producto al inventario."""
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad disponible del producto: "))
            break
        except ValueError:
            print("Precio y cantidad deben ser numéricos. Inténtalo de nuevo.")
    
    descripcion = input("Introduce la descripción del producto: ")
    
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad, 'descripcion': descripcion})
    print(f"Producto '{nombre}' añadido con éxito.")
def actualizar_producto():
    """Permite actualizar los detalles de un producto existente."""
    ver_productos()
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print(f"Actualizando '{producto['nombre']}'")
            nuevo_precio = input(f"Nuevo precio ({producto['precio']}): ")
            nueva_cantidad = input(f"Nuevo cantidad ({producto['cantidad']}): ")
            nueva_descripcion = input(f"Nueva descripción ({producto['descripcion']}): ")
            
            if nuevo_precio:
                try:
                    producto['precio'] = float(nuevo_precio)
                except ValueError:
                    print("El precio debe ser un valor numérico.")
            if nueva_cantidad:
                try:
                    producto['cantidad'] = int(nueva_cantidad)
                except ValueError:
                    print("La cantidad debe ser un valor numérico.")
            if nueva_descripcion:
                producto['descripcion'] = nueva_descripcion
                    
            print(f"Producto '{producto['nombre']}' actualizado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")
def eliminar_producto():
    """Elimina un producto basado en su nombre."""
    ver_productos()
    nombre = input("Introduce el nombre del producto que deseas eliminar: ")
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def ver_productos():
    """Muestra todos los productos en el inventario."""
    if productos:
        print("\nInventario de productos:")
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']} Gs, Cantidad: {producto['cantidad']}, Descripción: {producto['descripcion']}")
    else:
        print("No hay productos en el inventario.")
def menu():
    """Presenta el menú y maneja las opciones del usuario."""
    cargar_datos()  
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Iniciar el programa
menu()
