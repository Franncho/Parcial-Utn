import re
import json
import os

def clear_console() -> None:
    """
    It waits for the user to hit enter
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Presiona enter para continuar')
    os.system('cls')

def validar_entrada(entrada: str, patron: str):
    """
    Esta funcion valida la entrada del usuario utilizando una expresión regular.

    Parámetros:
        - entrada: La entrada del usuario a validar.
        - patron: Expresión regular que define el formato válido.

    Retorna:
        str: La entrada validada.
    """
    while not re.match (patron, entrada):
        print("entrada invalida. intente denuevo")
        entrada = input()
    return entrada

def imprimir_menu():
    menu=(
        "Bienvenido al programa!!\n"
        "1. Mostrar Nombre y posicion de los jugadores.\n"
        "2. Elegir un jugador y mostrar sus estadisticas.\n"
        "3. Guardar en csv el jugador de la opcion 2.\n"
        "4. Buscar el jugador y mostrar sus logros.\n"
        "5. Calcular promedio de puntos de todos los jugadores.\n"
        "6. Elegir el nombre de un jugador y ver si es del salon de la fama.\n"
        "7. Mostrar el jugador con la mayor cantidad de rebotes totales.\n"
        "8. Mostrar el jugador con el mayor porcentaje de tiros de campo.\n"
        "9. Mostrar el jugador con la mayor cantidad de asistencias totales.\n"
        "10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\n"
        "11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n"
        "12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\n"
        "13. Mostrar el jugador con la mayor cantidad de robos totales.\n"
        "14. Mostrar el jugador con la mayor cantidad de bloqueos totales.\n"
        "15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\n"
        "16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n"
        "17. Mostrar el jugador con la mayor cantidad de logros obtenidos\n"
        "18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n"
        "19. Mostrar el jugador con la mayor cantidad de temporadas jugadas\n"
        "20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n"
        "0. Salir del programa\n"
        "21. Limpiar consola\n" 
    )
    print(menu)





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

def mostrar_jugador_elegido_por_estadistica(jugadores: list, indice: int):

    print("Nombre {0}".format(jugadores[indice]["nombre"]))

    for atributo, valor in jugadores[indice]["estadisticas"].items():
        print("{0} : {1}". format(atributo, valor))

    return indice

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


def guardar_estadisticas_segun_indice_csv():
    pass

def buscar_por_nombre(jugadores: list, ingreso: str):
    contador = 0
    for jugador in jugadores:
        if re.search(jugador["nombre"][0:4], ingreso[0:4]) != None:
            print("sus logros son: ")
            for logro in jugador["logros"]:
                print("{0}".format(logro))
        else:
            contador += 1

    if contador == len(jugadores):
        print("Dato no encontrado")

def calcular_promedio(jugadores:list, key:str):
    suma=0
    contador=0

    if len(jugadores)>0:
        for jugador in jugadores:
                suma+=jugador["estadisticas"][key]
                contador+=1
        if contador>0:
            promedio=suma/contador
            print("El promedio general de {0} es {1} ".format(key, promedio))
    else:
        print("la lista esta vacia: ")
    return promedio

def calcular_y_mostrar_promedio_puntos_por_Partido(jugadores:list):
    pass

def verificar_salon_de_la_fama(jugadores:list, ingreso:str):
    miembro="Miembro del Salon de la Fama del Baloncesto"
    contador=0

    for jugador in jugadores:
        encontrado=False
        if re.search(jugador["nombre"][0:6], ingreso[0:6]) != None:
            if miembro in jugador["logros"]:
                print("{} es miembro del Salón de la Fama del Baloncesto".format(jugador["nombre"]))
                encontrado = True
            elif encontrado==False:
                print("{0} no pertenece al Salón de la Fama del Baloncesto.".format(jugador["nombre"]))

    if contador == len(jugadores):
        print("Dato no encontrado")


def calcular_key_totales(jugadores: list, key: str, flag: str):
    max_valor = None
    jugador_max = None

    for jugador in jugadores:
        estadistica_total = jugador["estadisticas"][key]

        if max_valor is None or (flag == "mayor" and estadistica_total > max_valor) or (flag == "menor" and estadistica_total < max_valor):
            max_valor = estadistica_total
            jugador_max = jugador

    if jugador_max is not None:
        print("El jugador con {0} cantidad de {1} es {2} con {3}".format(flag, key, jugador_max["nombre"], max_valor))
    else:
        print("No se encontró ningún jugador en la lista")

    return jugador_max

def mostrar_key_por_valor_dado(jugadores:list, ingreso:int, key):
    jugadores_superiores=[]

    for jugador in jugadores:
        nombre=jugador["nombre"]
        promedio_total=jugador["estadisticas"][key]

        if promedio_total>ingreso:
            jugadores_superiores.append(nombre)
    
    if len(jugadores_superiores)>0:
        print("Los siguientes jugadores tienen un {0} total mayor a {1} ".format(key,ingreso))
        for jugador in jugadores_superiores:
            print("Nombre: ",jugador)
    else:
        print("no hay jugadores de mayor promedio que {0} ".format(ingreso))


def mostrar_promedio_menos_el_menor(jugadores:list):
    minimo=calcular_key_totales(jugadores, "promedio_puntos_por_partido", "menor")
    lista_mayores=[]
    for jugador in jugadores:
        if jugador["estadisticas"]["promedio_puntos_por_partido"] > minimo["estadisticas"]["promedio_puntos_por_partido"]:
            lista_mayores.append(jugador)
    calcular_promedio(lista_mayores, "promedio_puntos_por_partido")

def calcular_mayor_logros(jugadores:list):
    max_logros=0
    jugador_max_logros=None

    for jugador in jugadores:
        logros_totales=len(jugador["logros"])

        if logros_totales > max_logros:
            max_logros=logros_totales
            jugador_max_logros=jugador

    if jugador_max_logros is not None:
        print("El jugador con mayor cantidad de logros es {0} con {1}".format(jugador_max_logros["nombre"], max_logros))
    else:
        print("No se encontró ningún jugador en la lista")