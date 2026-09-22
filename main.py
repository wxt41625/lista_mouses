'''
Nombre del estudiante: ______________________________
Grupo: ______________________________
Descripción del proyecto: Sistema de inventario de mouse
para un espacio de trabajo de Programación de Redes.
'''

import time

from datos import cargar_datos, guardar_datos
from operaciones import (
    agregar_elemento,
    mostrar_inventario,
    buscar_elemento,
    editar_elemento,
    eliminar_elemento,
    mostrar_stock_bajo,
    mostrar_resumen,
)


def mostrar_menu():
    # Muestra el menú principal.
    print("\n╔══════════════════════════════════════════════╗")
    print("║       INVENTARIO DE MOUSE - REDES           ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ 1. Agregar un nuevo mouse                   ║")
    print("║ 2. Mostrar inventario                       ║")
    print("║ 3. Buscar mouse por nombre o código         ║")
    print("║ 4. Editar cantidad o estado                 ║")
    print("║ 5. Eliminar un mouse                        ║")
    print("║ 6. Guardar y salir                          ║")
    print("║ 7. Mostrar mouse con stock bajo              ║")
    print("║ 8. Mostrar resumen del inventario            ║")
    print("║ 9. Salir sin guardar                        ║")
    print("╚══════════════════════════════════════════════╝")


def main():
    '''
    Función principal que ejecuta el programa de inventario.
    Muestra el menú y maneja la interacción con el usuario.
    '''

    # Lista principal donde se almacena el inventario.
    inventario = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ")

        match opcion:
            case '1':
                agregar_elemento(inventario)
                guardar_datos(inventario)
            case '2':
                mostrar_inventario(inventario)
            case '3':
                buscar_elemento(inventario)
            case '4':
                editar_elemento(inventario)
                guardar_datos(inventario)
            case '5':
                eliminar_elemento(inventario)
                guardar_datos(inventario)
            case '6':
                guardar_datos(inventario)
                print("Inventario guardado. Saliendo del programa.")
                break
            case '7':
                mostrar_stock_bajo(inventario)
            case '8':
                mostrar_resumen(inventario)
            case '9':
                print("Saliendo del programa sin guardar los últimos cambios.")
                break
            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.")

        time.sleep(1)


if __name__ == "__main__":
    main()
