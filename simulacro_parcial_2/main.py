"""
Listar los últimos N pokemones. El valor de N será ingresado por el usuario
(Validar que no supere max. de lista)

Ordenar y Listar pokemones por poder. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)

Ordenar y Listar pokemones por ID. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)

Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo), Preguntar qué 
promedio quiere calcular este esas posibles keys y filtrar los que cumplan con la condición de superar 
o no el promedio (preguntar al usuario la condición: menor o mayor) se deberá listar en consola aquellos
que cumplan con tener mayores o menores cantidades en la lista de dicha key según corresponda.

Buscar pokemones por tipo (dar e elegir los diversos tipos que un pokémon puede poseer, muchos de ellos
poseen más de un tipo, con lo cual habrá que darle a elegir al usuario entre todos los tipos que existen en 
el json) una vez seleccionado listar en consola los que posean dicho tipo. (Usando RegEx para la búsqueda).
Ejemplo: Si el usuario elige: volador y hay un pokemon con muchos tipos, pero uno de ellos es volador, 
deberá listarlo. (charizard, zapdos, moltres, articuno poseen más de un tipo, pero uno de ellos es volador).

Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]

"""
import func

def pokemon_app():
    lista_pokemon = func.cargar_json(r"C:\Users\maria\Documents\Programacion_UTN\ProgramacionUTN\simulacro_parcial_2\pokedex.json")
    while(True):
        respuesta = input("Ingrese un numero")
        if(respuesta == "1"):
            func.listar_pokemones(lista_pokemon)
        elif(respuesta == "2"):
            func.ordenar(lista_pokemon,"poder","desc")
        elif(respuesta == "3"):
            func.ordenar(lista_pokemon,"id","asc")
        elif(respuesta == "4"):
            func.calcular_promedio(lista_pokemon,"evoluciones","mayor")
        elif(respuesta == "5"):
            func.buscar(lista_pokemon)
        elif(respuesta == "6"):
           pass
        elif(respuesta == "7"):
            break

pokemon_app()