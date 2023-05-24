import re
import json


def parse_json(nombre_archivo: str):
    lista_jugadores = []
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        dict = json.load(archivo)
        lista_jugadores = dict["jugadores"]

    return lista_jugadores


ruta_archivo = r"C:\Users\rarug\Desktop\Parcial_python\dt.json"
lista_jugadores = parse_json(ruta_archivo)


print(lista_jugadores[0]["logros"][0])


# 1- Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
# Nombre Jugador - Posición. Ejemplo:
# Michael Jordan - Escolta

def mostrar_nombre_y_posicion(jugadores: list):

    for jugador in jugadores:
        if "nombre" in jugador and "posicion" in jugador:
            nombre = jugador["nombre"]
            posicion_jugador = jugador["posicion"]
            print("Nombre {0} - Posicion {1}".format(nombre, posicion_jugador))
        else:
            print("Dato no encontrado")


mostrar_nombre_y_posicion(lista_jugadores)

# 2-Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.


def mostar_jugador_elegido_por_estadistica(jugadores: list, indice: int):

    print("Nombre {0}".format(jugadores[indice]["nombre"]))

    for atributo, valor in jugadores[indice]["estadisticas"].items():
        print("{0} : {1}". format(atributo, valor))


ingreso = int(input("ingrese el indice del jugador: "))
mostar_jugador_elegido_por_estadistica(lista_jugadores, ingreso)


# 3-Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

def guardar_archivo(nombre_archivo: str, contenido: str):
    """
    Esta funcion guarda el contenido en un archivo con el nombre especificado.

    Parametros:
    - nombre_archivo: El nombre o ruta del archivo a guardar.
    - contenido: El contenido a guardar en el archivo.

    Retorna:
    - True si se guardó el archivo correctamente, False en caso contrario.
    """
    try:
        with open(nombre_archivo, "w+") as archivo:
            archivo.write(contenido)
        return True
    except:
        return False
    
def guardar_estadisticas_csv():
    pass