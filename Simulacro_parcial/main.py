"""
Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)

Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)

Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)

Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: menor o mayor) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.

Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

"""
import func


def stark_app():
    lista_heroes = func.cargar_json(r"C:\Users\maria\Documents\Programacion_UTN\ProgramacionUTN\Simulacro_parcial\data_stark (1).json")
    while(True):
        respuesta = input("Ingrese un numero")
        if(respuesta == "1"):
            func.listar_heroes(lista_heroes)
        elif(respuesta == "2"):
            func.ordenar(lista_heroes,"altura","desc")
        elif(respuesta == "3"):
            func.ordenar(lista_heroes,"fuerza","asc")
        elif(respuesta == "4"):
            func.calcular_promedio(lista_heroes,"altura","mayor")
        elif(respuesta == "5"):
            func.heroes_inteligencia(lista_heroes)
        elif(respuesta == "6"):
           func.exportar_csv(lista_heroes,r"C:\Users\maria\Documents\Programacion_UTN\ProgramacionUTN\Simulacro_parcial\heroes.csv")
        elif(respuesta == "7"):
            print("7 - Salir")
            break

stark_app()