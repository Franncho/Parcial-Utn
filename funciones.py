import re
import os


def clear_console() -> None:
    """
    It waits for the user to hit enter
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Presiona enter para continuar')
    os.system('cls')

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
        "21. Mostrar cuantos jugadores hay por posicion\n"
        "22. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente\n"
        "23. Mostrar que jugadores tienen mayor estadisticas en cada valor\n"
        "24. Mostrar el jugador con mayor estadisticas totales\n"
        "0. Salir del programa\n"
        "23. Limpiar consola\n" 
        "------------------------------------------------------------------------------------------------------------------------"
    )
    print(menu)

def validar_entero_regex(entrada):
    if re.match(r'^[0-9]+$', entrada):
        return int(entrada)
    else:
        print("Intente nuevamente")
        return None
    
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
def mostrar_jugador_elegido_con_estadisticas(jugadores: list, indice: int, flag:bool):
    """
    Esta funcion muestra la informacion de un jugador especifico según el indice dado.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        indice (int): El indice del jugador que se desea mostrar.

    Retorna:
        None
    """
    lista_estadisticas=[]

    if indice<=len(jugadores):
        print(jugadores[indice]["nombre"])
        print(jugadores[indice]["posicion"])

        for atributo, valor in jugadores[indice]["estadisticas"].items():
            lista_estadisticas.append("{0} : {1}".format(atributo,valor))
            if flag==True:
                print("{0} : {1}". format(atributo, valor))
                
        return lista_estadisticas
    else:
        print("No se puede acceder al indice que eligio. Intente denuevo")

#3
def guardar_estadisticas_segun_indice_csv(jugadores:list, indice:int):

    datos=jugadores[indice]["nombre"]
    jugador_elegido=mostrar_jugador_elegido_con_estadisticas(jugadores, indice, False)
    
    guardar_archivo("estadisticas_jugador_elegido.csv", "{0}, {1}".format(datos, "\n".join(jugador_elegido)))

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


def sort_alfabetico(jugadores: list, key: str, flag:bool):
    """
    Esta función ordena una lista de jugadores alfabéticamente según un atributo específico.

    Parámetros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
        key (str): El atributo por el cual se desea ordenar alfabéticamente.

    Retorna:
        list: Una nueva lista de jugadores ordenada alfabéticamente según el atributo dado, o una lista vacía si la entrada está vacía.
    """
    

    lista = jugadores[:]
    lista_derecha = []
    lista_izquierda = []

    if len(lista) <= 1:
        return lista
    
    else:
        for jugador in lista[1:]:
            
            if  flag==True and jugador[key] > lista[0][key] or flag== False and jugador[key] < lista[0][key]:
                lista_derecha.append(jugador)
            
            else:
                lista_izquierda.append(jugador)

    lista_izquierda = sort_alfabetico(lista_izquierda, key, flag)
    lista_derecha = sort_alfabetico(lista_derecha, key, flag)

    return lista_izquierda + [lista[0]] + lista_derecha

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
        jugadores_ordenados=sort_alfabetico(jugadores, "nombre", True)

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

        valor = None
        jugador_max_min = None

        for jugador in jugadores:
            estadistica_total = jugador["estadisticas"][key]

            if valor is None or (flag == "mayor" and estadistica_total > valor) or (flag == "menor" and estadistica_total < valor):
                valor = estadistica_total
                jugador_max_min = jugador

        if jugador_max_min is not None:
            print("El jugador con {0} cantidad de {1} es {2} con {3}".format(flag, key, jugador_max_min["nombre"], valor))
        else:
            print("No se encontró ningún jugador en la lista")

        return jugador_max_min

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
        list: Una lista de diccionarios que representan a los jugadores que tienen un valor mayor que el ingreso para la clave especificada.
    """
    if len(jugadores)>0:

        jugadores_superiores=[]

        for jugador in jugadores:
            estadistica=jugador["estadisticas"][key]

            if estadistica>ingreso:
                jugadores_superiores.append(jugador)
        
        if len(jugadores_superiores) > 0:
            print("Los siguientes jugadores tienen un {0} total mayor a {1} ".format(key,ingreso))

            for jugador in jugadores_superiores:
                print("Nombre: ",jugador["nombre"], jugador["estadisticas"][key])

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
    jugadores_ordenados = sort_alfabetico(jugadores, "posicion", True)
    key_dada=mostrar_key_por_valor_dado(jugadores, ingreso, "porcentaje_tiros_de_campo")

    print("Jugadores ordenados alfabéticamente por posición:")

    for jugador in jugadores_ordenados:

        for lista in key_dada:
            if jugador["nombre"] == lista["nombre"]: 
                print("Nombre: {0} Posición: {1}, Porcentaje de tiros de campo {2}:".format(jugador["nombre"],jugador["posicion"], jugador["estadisticas"]["porcentaje_tiros_de_campo"]))


#Extras

#1
def contar_jugadores_por_posicion(jugadores:list):
    """
    Esta funcion cuenta la cantidad de jugadores por cada posicion en una lista de jugadores.

    Parámetros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.

    Retorna:
        dict: Un diccionario donde las claves son las posiciones y los valores son la cantidad de jugadores en esa posición.
    """
    jugadores_por_posicion={}
    if len(jugadores)>0:
        for jugador in jugadores:
            posicion=jugador["posicion"]
            if posicion in jugadores_por_posicion:
                jugadores_por_posicion[posicion]+=1
            else:
                jugadores_por_posicion[posicion]=1

        return jugadores_por_posicion
    else:
        print("la lista esta vacia")

#2
def mostrar_jugadores_all_star(jugadores:list):
    """
    Esta funcion muestra los jugadores ordenados alfabeticamente por la cantidad de veces que han sido seleccionados para el All-Star Game.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.

    Retorna:
        list: Una lista de diccionarios de jugadores ordenados alfabéticamente por la cantidad de veces en All-Star.

    """

    lista_aux_jugadores = []
    if len(jugadores)>0:
        for jugador in jugadores:
            diccionario_jugador = {}
            diccionario_jugador["nombre"] = jugador["nombre"]
            for logros in jugador["logros"]:
                if re.search(r"^[0-9] +veces All-Star$|^[0-9][0-9] +veces All-Star$",logros):
                    cantidad = logros[:2]
                    cantidad = int(cantidad)
                    diccionario_jugador["logros"] = cantidad
                    lista_aux_jugadores.append(diccionario_jugador)
                            
        lista_aux_jugadores = sort_alfabetico(lista_aux_jugadores,"logros", False)

        return lista_aux_jugadores
    
    else:
        print("la lista esta vacia")

#3
def mejores_estadisticas_cada_valor(jugadores:list):
    """
    Esta funcion calcula y muestra el jugador con la mayor cantidad en cada estadística específica.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.
    
    Retorna:
        None

    """
    calcular_key_totales(jugadores, "temporadas", "mayor")
    calcular_key_totales(jugadores, "puntos_totales", "mayor")
    calcular_key_totales(jugadores, "promedio_puntos_por_partido", "mayor")
    calcular_key_totales(jugadores, "rebotes_totales", "mayor")
    calcular_key_totales(jugadores, "promedio_rebotes_por_partido", "mayor")
    calcular_key_totales(jugadores, "asistencias_totales", "mayor")
    calcular_key_totales(jugadores, "promedio_asistencias_por_partido", "mayor")
    calcular_key_totales(jugadores, "robos_totales", "mayor")
    calcular_key_totales(jugadores, "bloqueos_totales", "mayor")
    calcular_key_totales(jugadores, "porcentaje_tiros_de_campo", "mayor")
    calcular_key_totales(jugadores, "porcentaje_tiros_libres", "mayor")
    calcular_key_totales(jugadores, "porcentaje_tiros_triples", "mayor")

#4
def mejores_estadisticas(jugadores:list):
    """
    Esta funcion calcula y muestra el jugador que tiene las mejores estadisticas de todos los jugadores en la lista.

    Parametros:
        jugadores (list): Una lista de diccionarios que representan a los jugadores.

    Retorna:
        None
    """
    jugador_max=None
    max_puntaje=0
    if len(jugadores)>0:

        for jugador in jugadores:
            estadistica_total=0
            for estadistica in jugador["estadisticas"].values():
                estadistica_total+=estadistica

            if jugador_max is None or estadistica_total < max_puntaje:
                jugador_max=jugador
        print("el jugador que tiene mejores estadisticas es: {0}".format(jugador_max["nombre"]))

    else:
        print("la lista esta vacia")
    
