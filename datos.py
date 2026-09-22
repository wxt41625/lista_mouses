import json

# Archivo donde se guardan los datos del inventario.
ARCHIVO_DATOS = "dispositivos.json"


def cargar_datos():
    '''
    Función para cargar datos del inventario desde el archivo JSON.
    Maneja archivo inexistente, vacío o con JSON incorrecto.
    '''
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

            if not contenido.strip():
                print("El archivo está vacío. Se iniciará un inventario nuevo.")
                return []

            return json.loads(contenido)

    except FileNotFoundError:
        print("No se encontró el archivo. Se iniciará un inventario nuevo.")
        return []
    except json.JSONDecodeError:
        print("Error: el archivo JSON es incorrecto. Se iniciará un inventario nuevo.")
        return []


def guardar_datos(inventario):
    '''
    Función para guardar los datos del inventario.
    '''
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(inventario, archivo, indent=4, ensure_ascii=False)
    except OSError:
        print("Error: no se pudo guardar el archivo del inventario.")
