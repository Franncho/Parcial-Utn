from funciones import *
import json

def parse_json(nombre_archivo: str):
    lista_jugadores = []
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        dict = json.load(archivo)
        lista_jugadores = dict["jugadores"]

    return lista_jugadores


ruta_archivo = r"C:\Users\rarug\Desktop\Parcial_python\dt.json"
lista_jugadores = parse_json(ruta_archivo)

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
        calcular_key_totales(lista_jugadores, "rebotes_totales", "mayor")

    elif opcion == "8":
        calcular_key_totales(lista_jugadores, "porcentaje_tiros_de_campo", "mayor")

    elif opcion == "9":
        calcular_key_totales(lista_jugadores, "asistencias_totales", "mayor")

    elif opcion == "10":
        ingreso = int(input("ingrese un valor: "))
        mostrar_key_por_valor_dado(lista_jugadores, ingreso, "promedio_puntos_por_partido")

    elif opcion == "11":
        ingreso = int(input("ingrese un valor: "))
        mostrar_key_por_valor_dado(lista_jugadores, ingreso, "promedio_rebotes_por_partido")

    elif opcion == "12":
        ingreso = int(input("ingrese un valor: "))
        mostrar_key_por_valor_dado(lista_jugadores, ingreso, "promedio_asistencias_por_partido")

    elif opcion == "13":
        calcular_key_totales(lista_jugadores, "robos_totales", "mayor")

    elif opcion == "14":
        calcular_key_totales(lista_jugadores, "bloqueos_totales", "mayor")

    elif opcion == "15":
        ingreso = int(input("ingrese un valor: "))
        mostrar_key_por_valor_dado(lista_jugadores, ingreso, "porcentaje_tiros_libres")

    elif opcion == "16":
        mostrar_promedio_menos_el_menor(lista_jugadores)

    elif opcion == "17":
        calcular_mayor_logros(lista_jugadores)

    elif opcion == "18":
        ingreso = int(input("ingrese un valor: "))
        mostrar_key_por_valor_dado(lista_jugadores, ingreso, "porcentaje_tiros_triples")

    elif opcion == "19":
        calcular_key_totales(lista_jugadores, "temporadas", "mayor")

    elif opcion == "20":
        ingreso = int(input("ingrese un valor: "))
        ordenar_posiciones(lista_jugadores, ingreso)

    elif opcion == "21":
        clear_console()

    elif opcion == "0":
        print("Adios, hasta la proxima!!!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
        
    print("------------------------------------------------------------------------------------------------------------------------")
    input("Apriete enter para seguir ")