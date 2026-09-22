import time


# Estados permitidos para los mouse.
ESTADOS = ["Bueno", "Regular", "Dañado", "En reparación"]


def mostrar_inventario(inventario):
    '''
    Función que recibe una lista de inventario y muestra cada elemento
    en formato de tabla.
    '''
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n+-------------+------------------------------+----------+-----------------+-----------------+")
    print("| codigo      | nombre                       | cantidad | estado          | ubicacion       |")
    print("+-------------+------------------------------+----------+-----------------+-----------------+")

    for elemento in inventario:
        print(
            f"| {elemento['codigo']:<11} "
            f"| {elemento['nombre']:<28} "
            f"| {elemento['cantidad']:<8} "
            f"| {elemento['estado']:<15} "
            f"| {elemento['ubicacion']:<15} |"
        )

    print("+-------------+------------------------------+----------+-----------------+-----------------+")


def agregar_elemento(inventario):
    '''
    Función para agregar un mouse a la lista del inventario.
    '''
    print("\n--- Agregar mouse ---")

    codigo = input("Ingrese el código del mouse: ").strip()
    nombre = input("Ingrese el nombre del mouse: ").strip()
    ubicacion = input("Ingrese la ubicación: ").strip()

    if codigo == "" or nombre == "" or ubicacion == "":
        print("Error: los textos no pueden estar vacíos.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad < 0:
            print("Error: la cantidad no puede ser negativa.")
            return
    except ValueError:
        print("Error: la cantidad debe ser un número entero.")
        return

    estado = input("Ingrese el estado (Bueno, Regular, Dañado, En reparación): ").strip()

    if estado not in ESTADOS:
        print("Error: el estado no es válido.")
        print("Estados permitidos:", ", ".join(ESTADOS))
        return

    # Se crea el diccionario del nuevo registro.
    mouse = {
        "codigo": codigo,
        "nombre": nombre,
        "cantidad": cantidad,
        "estado": estado,
        "ubicacion": ubicacion
    }

    inventario.append(mouse)
    print("Mouse agregado exitosamente.")


def buscar_elemento(inventario):
    '''
    Busca un mouse por código o nombre sin distinguir mayúsculas y minúsculas.
    '''
    dato = input("Ingrese el código o nombre del mouse a buscar: ").strip()

    if dato == "":
        print("Error: el dato de búsqueda no puede estar vacío.")
        return

    encontrado = False

    for elemento in inventario:
        if (dato.lower() in elemento["codigo"].lower() or
                dato.lower() in elemento["nombre"].lower()):
            print(
                f"Código: {elemento['codigo']} | "
                f"Nombre: {elemento['nombre']} | "
                f"Cantidad: {elemento['cantidad']} | "
                f"Estado: {elemento['estado']} | "
                f"Ubicación: {elemento['ubicacion']}"
            )
            encontrado = True

    if not encontrado:
        print("No se encontró ningún mouse con ese dato.")


def editar_elemento(inventario):
    '''
    Busca un mouse por código y permite modificar cantidad y estado.
    '''
    codigo = input("Ingrese el código del mouse a editar: ").strip()

    for elemento in inventario:
        if elemento["codigo"].lower() == codigo.lower():
            try:
                elemento["cantidad"] = int(input("Nueva cantidad: "))

                if elemento["cantidad"] < 0:
                    print("Error: la cantidad no puede ser negativa.")
                    return

            except ValueError:
                print("Error: la cantidad debe ser un número entero.")
                return

            nuevo_estado = input(
                "Nuevo estado (Bueno, Regular, Dañado, En reparación): "
            ).strip()

            if nuevo_estado not in ESTADOS:
                print("Error: el estado no es válido.")
                return

            elemento["estado"] = nuevo_estado
            time.sleep(1)
            print("Mouse actualizado.")
            return

    print("No se encontró un mouse con ese código.")


def eliminar_elemento(inventario):
    '''
    Busca un mouse por código y lo elimina de la lista con remove().
    '''
    codigo = input("Ingrese el código del mouse a eliminar: ").strip()

    for elemento in inventario:
        if elemento["codigo"].lower() == codigo.lower():
            inventario.remove(elemento)
            time.sleep(1)
            print("Mouse eliminado.")
            return

    print("No se encontró un mouse con ese código.")


def mostrar_stock_bajo(inventario):
    '''
    Muestra los mouse que tienen una cantidad de 2 o menos.
    '''
    encontrado = False

    print("\n--- Mouse con stock bajo ---")

    for elemento in inventario:
        if elemento["cantidad"] <= 2:
            print(
                f"{elemento['codigo']} - {elemento['nombre']} - "
                f"Cantidad: {elemento['cantidad']}"
            )
            encontrado = True

    if not encontrado:
        print("No hay mouse con stock bajo.")


def mostrar_resumen(inventario):
    '''
    Muestra un resumen de cuantos mouse hay en cada estado.
    '''
    if not inventario:
        print("El inventario está vacío.")
        return

    estados = {}

    for elemento in inventario:
        estado = elemento["estado"]

        if estado in estados:
            estados[estado] += elemento["cantidad"]
        else:
            estados[estado] = elemento["cantidad"]

    print("\n--- Resumen del inventario ---")
    for estado, cantidad in estados.items():
        print(f"{estado}: {cantidad} mouse")
