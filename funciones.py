import re
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
        "------------------------------------------------------------------------------------------------------------------------"
    )
    print(menu)

#1
def mostrar_nombre_y_posicion(jugadores: list):
    """
    Esta funcion muestra el nombre y la posicion de cada jugador en la lista de jugadores.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.

    Retorna:
        None
    """
    if len(jugadores)>0:
        
        for jugador in jugadores:
            if "nombre" in jugador and "posicion" in jugador:
                nombre = jugador["nombre"]
                posicion_jugador = jugador["posicion"]
                print("Nombre {0} - Posicion {1}".format(nombre, posicion_jugador))
            else:
                print("Dato no encontrado")
    else:
        print("La lista se encuentra vacia")

#2
def mostrar_jugador_elegido_por_estadistica(jugadores: list, indice: int):

    """
    Esta funcion muestra la informacion de un jugador especifico según el indice dado.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        indice (int): El indice del jugador que se desea mostrar.

    Retorna:
        int: El indice del jugador mostrado.
    """

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

#3
def guardar_estadisticas_segun_indice_csv():
    pass

#4
def buscar_por_nombre(jugadores: list, ingreso: str):
    """
    Esta funcion busca jugadores por nombre y muestra sus logros si se encuentra una coincidencia.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        ingreso (str): El nombre o parte del nombre a buscar.
    
    Retorna:
        None
    """
    contador = 0
    if len(jugadores)>0:
        for jugador in jugadores:
            if re.search(jugador["nombre"][0:4], ingreso[0:4]) != None:
                print("sus logros son: ")
                for logro in jugador["logros"]:
                    print("{0}".format(logro))
            else:
                contador += 1

        if contador == len(jugadores):
            print("Dato no encontrado")
    else:
        print("la lista esta vacia")

def calcular_promedio(jugadores: list, key: str):
    """
    Esta función calcula el promedio de un atributo específico de las estadísticas de los jugadores.

    Parámetros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        key (str): El atributo de las estadísticas a promediar.

    Retorna:
        float: El promedio del atributo dado.

    """
    suma = 0
    contador = 0

    if len(jugadores) > 0:
        for jugador in jugadores:
            if key in jugador["estadisticas"]:
                suma += jugador["estadisticas"][key]
                contador += 1

        if contador > 0:
            promedio = suma / contador
            print("El promedio general de {0} es {1}".format(key, promedio))
        else:
            print("No se encontraron datos para calcular el promedio de {0}".format(key))
            promedio=0
    else:
        print("La lista de jugadores está vacía")
        promedio=0

    return promedio


def sort_alfabetico(jugadores: list, key: str):
    """
    Esta función ordena una lista de jugadores alfabéticamente según un atributo específico.

    Parámetros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        key (str): El atributo por el cual se desea ordenar alfabéticamente.

    Retorna:
        list: Una nueva lista de jugadores ordenada alfabéticamente según el atributo dado, o una lista vacía si la entrada está vacía.
    """
    if len(jugadores) > 0:
        lista = jugadores[:]
        lista_derecha = []
        lista_izquierda = []

        if len(lista) <= 1:
            return lista
        else:
            for jugador in lista[1:]:
                if jugador[key] > lista[0][key]:
                    lista_derecha.append(jugador)
                else:
                    lista_izquierda.append(jugador)

        lista_izquierda = sort_alfabetico(lista_izquierda, key)
        lista_derecha = sort_alfabetico(lista_derecha, key)

        return lista_izquierda + [lista[0]] + lista_derecha
    else:
        print("La lista está vacía")
        return []  # Devuelve una lista vacia si la entrada esta vacia


#5
def calcular_y_mostrar_promedio_puntos_por_Partido(jugadores:list):
    """
    Esta funcion calcula y muestra el promedio de puntos por partido para una lista de jugadores, y luego muestra los jugadores
    ordenados alfabeticamente.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
    
    Retorna:
        None

    """
    if len(jugadores)>0:

        promedio=calcular_promedio(jugadores, "promedio_puntos_por_partido")
        jugadores_ordenados=sort_alfabetico(jugadores, "nombre")

        print("Promedio general de puntos por partido: {0}".format(promedio))
        print("Jugadores ordenados alfabéticamente:")

        for jugador in jugadores_ordenados:
            print("Nombre: {0}, Promedio de puntos por partido: {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))
    else:
        print("la lista esta vacia")   
#6
def verificar_salon_de_la_fama(jugadores:list, ingreso:str):
    """
    Esta funcion verifica si un jugador pertenece al Salon de la Fama del Baloncesto, utilizando una lista de jugadores y un dato
    de ingreso.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        ingreso (str): El dato de ingreso a comparar con los nombres de los jugadores.

    Retorna:
        None
    """
    if len(jugadores)>0:
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

#7, 8, 9, 13, 14, 19
def calcular_key_totales(jugadores: list, key: str, flag: str):
    """
    Esta funcion calcula y muestra el jugador con la mayor o menor cantidad de una estadistica especifica en una lista de jugadores.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        key (str): La clave (key) de la estadistica a comparar.
        flag (str): La bandera (flag) que indica si se busca el mayor ("mayor") o menor ("menor") valor.

    Retorna:
        dict: El diccionario del jugador con la mayor o menor cantidad de la estadistica especifica.

    """
    if len(jugadores)>0:
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
    else:
        print("La lista esta vacia")

#10, 11, 12, 15, 18, 20
def mostrar_key_por_valor_dado(jugadores:list, ingreso:int, key:str):
    """
    Esta funcion muestra los jugadores que tienen un valor mayor que el valor dado para una clave específica.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        ingreso (int): El valor de referencia para comparar.
        key (str): La clave (key) de la estadistica a comparar.

    Retorna:
        None
    """
    if len(jugadores)>0:
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
                
            return jugadores_superiores
        else:
            print("no hay jugadores de mayor {0} que {1} ".format(key,ingreso))
    else:
        print("La lista esta vacia")

#16
def mostrar_promedio_menos_el_menor(jugadores:list):
    """
    Esta funcion calcula y muestra el promedio general de puntos por partido restando el valor mas bajo encontrado.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.

    Retorna:
        None
    """
    if len(jugadores)>0:
        minimo = calcular_key_totales(jugadores, "promedio_puntos_por_partido", "menor")
        lista_mayores = []

        for jugador in jugadores:
            if jugador["estadisticas"]["promedio_puntos_por_partido"] > minimo["estadisticas"]["promedio_puntos_por_partido"]:
                lista_mayores.append(jugador)

        calcular_promedio(lista_mayores, "promedio_puntos_por_partido")
    else:
        print("la lista esta vacia")

#17
def calcular_mayor_logros(jugadores:list):
    """
    Esta funcion calcula y muestra el jugador con la mayor cantidad de logros.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.

    Retorna:
        None
    """
    if len(jugadores)>0:
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
    else:
        print("La lista esta vacia")

#20
def ordenar_posiciones(jugadores: list, ingreso: int):
    """
    Esta funcion ordena y muestra la informacion de los jugadores por posicion, y muestra su porcentaje de tiros de campo.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        ingreso (int): Un valor entero que representa el limite minimo del porcentaje de tiros de campo.
    
    Retorna:
        None
    """
    jugadores_ordenados = sort_alfabetico(jugadores, "posicion")
    key_dada = mostrar_key_por_valor_dado(jugadores, ingreso, "porcentaje_tiros_de_campo")

    print("Jugadores ordenados alfabéticamente por posición:")

    for jugador in jugadores_ordenados:
        porcentaje_tiros=jugador["estadisticas"][key_dada]
        print("Nombre: {0}, Posición: {1}, Porcentaje de tiros de campo: {2}".format(jugador["nombre"], jugador["posicion"], porcentaje_tiros))