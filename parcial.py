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


def parse_json(nombre_archivo: str):
    lista_jugadores = []
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        dict = json.load(archivo)
        lista_jugadores = dict["jugadores"]

    return lista_jugadores


ruta_archivo = r"C:\Users\rarug\Desktop\Parcial_python\dt.json"
lista_jugadores = parse_json(ruta_archivo)


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


# mostrar_nombre_y_posicion(lista_jugadores)

# 2-Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.


def mostrar_jugador_elegido_por_estadistica(jugadores: list, indice: int):

    print("Nombre {0}".format(jugadores[indice]["nombre"]))

    for atributo, valor in jugadores[indice]["estadisticas"].items():
        print("{0} : {1}". format(atributo, valor))

    return indice


# ingreso = int(input("ingrese el indice del jugador: "))
# mostrar_jugador_elegido_por_estadistica(lista_jugadores, ingreso)


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


# 4-Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.

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


# ingreso = input("ingrese el jugador a buscar: ").lower().capitalize()
# buscar_por_nombre(lista_jugadores, ingreso)

# Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente

def calcular_promedio(jugadores:list, key:str):
    suma=0
    contador=0

    if len(jugadores)>0:
        for jugador in jugadores:
            if key in jugador:
                suma+=jugador[key]
                contador+=1
        if contador>0:
            promedio=suma/contador
            print("El promedio general de {0} es {1} ".format(key, promedio))
    else:
        print("la lista esta vacia: ")

def calcular_y_mostrar_promedio_puntos_por_Partido(jugadores:list):
    calcular_promedio(jugadores, ["promedio_puntos_por_partido"])
        



# calcular_y_mostrar_promedio_puntos_por_Partido(lista_jugadores)

# Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.

def verificar_salon_de_la_fama(jugadores:list, ingreso:str):
    encontrado=False
    miembro="Miembro del Salon de la Fama del Baloncesto"
    contador=0

    for jugador in jugadores:
        if re.search(jugador["nombre"][0:4], ingreso[0:4]) != None:
            if miembro in jugador["logros"]:
                print("{} es miembro del Salón de la Fama del Baloncesto".format(jugador["nombre"]))
                encontrado = True
            elif encontrado==False:
                print("{0} no pertenece al Salón de la Fama del Baloncesto.".format(jugador["nombre"]))

    if contador == len(jugadores):
        print("Dato no encontrado")
        
# Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.

def calcular_key_totales(jugadores:list, key:str):
    jugador_max=None
    max_key=0
    for jugador in jugadores:
        nombre=jugador["nombre"]
        estadistica_total=jugador["estadisticas"][key]

        if estadistica_total >max_key:
            max_key=estadistica_total
            jugador_max=nombre
    print("El jugador con mayor cantidad de asistencias es {0} con {1} ".format(jugador_max, max_key))

# 10-Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.

def mostrar_promedio_puntos_por_valor(jugadores:list, ingreso:int):
    contador=0
    for jugador in jugadores:
        nombre=jugador["nombre"]
        promedio=calcular_promedio(jugador, "promedio_puntos_por_partido")

        if promedio>ingreso:
            contador+=1
            print("{0} tiene/n mas promedio de puntos totales que el valor dado ".format(nombre))





while True:

    imprimir_menu()

    opcion = input("Ingrese la opcion deseada: ")
    # opcion = validar_entrada(opcion, r"^[0-21]$")

    if opcion == "1":
        mostrar_nombre_y_posicion(lista_jugadores)

    elif opcion == "2":
        ingreso = int(input("ingrese el indice del jugador: "))
        mostrar_jugador_elegido_por_estadistica(lista_jugadores, ingreso)

    elif opcion == "3":
        pass

    elif opcion == "4":
        ingreso = input("ingrese el nombre del jugador a buscar: ").lower().capitalize()
        buscar_por_nombre(lista_jugadores, ingreso)

    elif opcion == "5":
        calcular_y_mostrar_promedio_puntos_por_Partido(lista_jugadores)
    
    elif opcion == "6":
        ingreso = input("ingrese el nombre del jugador a buscar: ").lower().capitalize()
        verificar_salon_de_la_fama(lista_jugadores, ingreso)

    elif opcion == "7":
        calcular_key_totales(lista_jugadores, "rebotes_totales")

    elif opcion == "8":
        calcular_key_totales(lista_jugadores, "porcentaje_tiros_de_campo")

    elif opcion == "9":
        calcular_key_totales(lista_jugadores, "asistencias_totales")

    elif opcion == "10":
        ingreso = int(input("ingrese un valor: "))
        mostrar_promedio_puntos_por_valor(lista_jugadores, ingreso)

    elif opcion == "11":
        pass

    elif opcion == "12":
        pass

    elif opcion == "13":
        calcular_key_totales(lista_jugadores, "robos_totales")

    elif opcion == "14":
        calcular_key_totales(lista_jugadores, "bloqueos_totales")

    elif opcion == "15":
        pass

    elif opcion == "16":
        pass

    elif opcion == "17":
        pass

    elif opcion == "18":
        pass

    elif opcion == "19":
        calcular_key_totales(lista_jugadores, "temporadas")

    elif opcion == "20":
        pass

    elif opcion == "21":
        clear_console()

    elif opcion == "0":
        print("Adios, hasta la proxima!!!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")

        input("Apriete enter para seguir ")


