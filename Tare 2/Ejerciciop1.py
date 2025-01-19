ventas = [
    {
        "fecha": "12-01-2023",
        "producto": "Producto_A",
        "cantidad": 50,
        "precio": 45.00,
        "promocion": True
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_AX",
        "cantidad": 160,
        "precio": 12.00,
        "promocion": False
    },
    {
        "fecha": "10-01-2023",
        "producto": "Producto_D",
        "cantidad": 20,
        "precio": 15.00,
        "promocion": False
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_C",
        "cantidad": 10,
        "precio": 140.00,
        "promocion": False
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_D",
        "cantidad": 1200,
        "precio": 1.00,
        "promocion": True
    }
]

def mostrar_listado_ventas():
    print("\nListado de ventas:")
    for venta in ventas:
        print(venta)

def anadir_producto():
    fecha = input("Ingrese la fecha (dd-mm-aaaa): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    promocion = input("¿Tiene promoción? (True/False): ").capitalize() == "True"

    nueva_venta = {
        "fecha": fecha,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "promocion": promocion
    }
    ventas.append(nueva_venta)
    print("\nProducto añadido exitosamente!")

def calcular_suma_total():
    suma_total = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    print(f"\nLa suma total de las ventas es: {suma_total:.2f}")

def calcular_promedio_ventas():
    total_ventas = len(ventas)
    suma_total = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    promedio = suma_total / total_ventas if total_ventas > 0 else 0
    print(f"\nEl promedio de ventas es: {promedio:.2f}")

def producto_mas_vendido():
    producto_max = max(ventas, key=lambda venta: venta["cantidad"])
    print(f"\nEl producto con más unidades vendidas es: {producto_max['producto']} ({producto_max['cantidad']} unidades)")

def mostrar_listado_productos():
    productos = list({venta["producto"] for venta in ventas})
    print("\nListado de productos:")
    for producto in productos:
        print(producto)

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar el listado de ventas")
        print("2. Añadir un producto")
        print("3. Calcular la suma total de las ventas")
        print("4. Calcular el promedio de ventas")
        print("5. Mostrar el producto con más unidades vendidas")
        print("6. Mostrar el listado de productos")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            mostrar_listado_ventas()
        elif opcion == "2":
            anadir_producto()
        elif opcion == "3":
            calcular_suma_total()
        elif opcion == "4":
            calcular_promedio_ventas()
        elif opcion == "5":
            producto_mas_vendido()
        elif opcion == "6":
            mostrar_listado_productos()
        elif opcion == "7":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

# Ejecutar el menú
menu()
