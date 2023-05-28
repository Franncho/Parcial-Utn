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

    opcion =input("Ingrese la opcion deseada: ")

    if re.match(r'^[0-9]+$', opcion):
        opcion=int(opcion)
        match(opcion):
            case 1:
                mostrar_nombre_y_posicion(lista_jugadores)

            case 2:
                ingreso = int(input("ingrese el indice del jugador: "))
                mostrar_jugador_elegido_con_estadisticas(lista_jugadores, ingreso)

            case 3:
                pass

            case 4:
                ingreso = input("ingrese el nombre del jugador a buscar: ").lower().capitalize()
                buscar_por_nombre(lista_jugadores, ingreso)

            case 5:
                if len(lista_jugadores)>0:
                    calcular_y_mostrar_promedio_puntos_por_Partido(lista_jugadores)
                else:
                    print("la lista esta vacia")
                
            case 6:
                ingreso = input("ingrese el nombre del jugador a buscar: ").lower().capitalize()
                verificar_salon_de_la_fama(lista_jugadores, ingreso)
            
            case 7:
                calcular_key_totales(lista_jugadores, "rebotes_totales", "mayor")
            
            case 8:
                calcular_key_totales(lista_jugadores, "porcentaje_tiros_de_campo", "mayor")
            
            case 9:
                calcular_key_totales(lista_jugadores, "asistencias_totales", "mayor")

            case 10:
                ingreso = input("Ingrese un valor: ")
                ingreso_validado = validar_entero_regex(ingreso)

                if ingreso_validado is not None:
                    mostrar_key_por_valor_dado(lista_jugadores, ingreso_validado, "promedio_puntos_por_partido")
                

            case 11:
                ingreso = input("ingrese un valor: ")
                ingreso_validado = validar_entero_regex(ingreso)

                if ingreso_validado is not None:
                    mostrar_key_por_valor_dado(lista_jugadores, ingreso, "promedio_rebotes_por_partido")
                

            case 12:
                ingreso = input("ingrese un valor: ")
                ingreso_validado = validar_entero_regex(ingreso)

                if ingreso_validado is not None:
                    mostrar_key_por_valor_dado(lista_jugadores, ingreso, "promedio_asistencias_por_partido")
                
            
            case 13:
                calcular_key_totales(lista_jugadores, "robos_totales", "mayor")

            case 14:
                calcular_key_totales(lista_jugadores, "bloqueos_totales", "mayor")
            
            case 15:
                ingreso = input("ingrese un valor: ")
                ingreso_validado = validar_entero_regex(ingreso)

                if ingreso_validado is not None:
                    mostrar_key_por_valor_dado(lista_jugadores, ingreso, "porcentaje_tiros_libres")

            case 16:
                calcular_mayor_logros(lista_jugadores)
            
            case 17:
                calcular_mayor_logros(lista_jugadores)

            case 18:
                ingreso = input("ingrese un valor: ")
                ingreso_validado = validar_entero_regex(ingreso)

                if ingreso_validado is not None:
                    mostrar_key_por_valor_dado(lista_jugadores, ingreso, "porcentaje_tiros_triples")

            case 19:
                calcular_key_totales(lista_jugadores, "temporadas", "mayor")
            
            case 20:
                if len(lista_jugadores)>0:
                        ingreso = int(input("ingrese un valor: "))
                        ordenar_posiciones(lista_jugadores, ingreso)
                else:
                    print("la lista esta vacia")
            
            case 21:
                clear_console()
            
            case 0:
                print("Adios, hasta la proxima!!!")
            
            case _:
                print("Opcion no valida. Intente denuevo")
        print("------------------------------------------------------------------------------------------------------------------------")
        input("Presione Enter para continuar")

    else:
        print("Ingrese una opcion numerica")
        input("Presione Enter para continuar")
        
