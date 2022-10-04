import json
import re


def cargar_json(path:str)->list:
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["heroes"]

def validar_entero(numero_str:str)->int:
    result = re.match("^[0-9]+$",numero_str)
    if(result != None):
        return int(numero_str)
    else:
        return False

def buscar_maximo(lista_maximo,key:str)-> int:
    maximo = 0
    for i in range(len(lista_maximo)):
        if(lista_maximo[i][key] > lista_maximo[maximo][key]):
            maximo = i 
    return maximo

def buscar_minimo(lista_minimo,key:str)->int:
    minimo = 0
    for i in range(len(lista_minimo)):
        if(lista_minimo[i][key] < lista_minimo[minimo][key]):
            minimo = i
    return minimo

def listar_heroes(lista_personajes:list):
    numero_heroes = input("Ingrese el numero de heroes")
    numero_heroes = validar_entero(numero_heroes)
    if(numero_heroes != False):
        if(numero_heroes > len(lista_personajes)):
            print("Error")
        else:
            for i in range(numero_heroes):
                print(lista_personajes[i])
            return lista_personajes
           
def ordenar(lista_personajes:list,key:str,orden:str)-> list:
    
    lista_duplicada = lista_personajes.copy()
    lista_ordenada = []

    while(len(lista_duplicada) > 0):
        if(orden == "asc"):
            indice_maximo = buscar_maximo(lista_duplicada,key)
            elemento_maximo = lista_duplicada.pop(indice_maximo)
            lista_ordenada.append(elemento_maximo)

        elif(orden == "desc"):
            indice_minimo = buscar_minimo(lista_duplicada,key)
            elemento_minimo = lista_duplicada.pop(indice_minimo)
            lista_ordenada.append(elemento_minimo)

    for heroe in lista_ordenada:
        print(heroe["nombre"],heroe[key])
    return lista_ordenada

def calcular_promedio(lista_personajes,key:str,condicion:str)-> list:
    acumulador_key = 0
    lista_condicion = []

    for heroe in lista_personajes:
        acumulador_key = acumulador_key + heroe[key]
    promedio_key = acumulador_key / len(lista_personajes)

    print(promedio_key)

    for heroe in lista_personajes:
        if(condicion == "menor" and heroe[key] < promedio_key):
            lista_condicion.append(heroe)
        elif(condicion == "mayor" and heroe[key] > promedio_key):
            lista_condicion.append(heroe)
    print(lista_condicion)
    return lista_condicion

def heroes_inteligencia(lista_personajes) ->list:
    patron = input("Que tipo de inteligencia desea?")
    lista_inteligencia = []
    for heroe in lista_personajes:
        if(re.search(patron,heroe["inteligencia"],re.IGNORECASE)):
            lista_inteligencia.append(heroe["nombre"])
    print(lista_inteligencia)
    return lista_inteligencia

def exportar_csv(lista_personajes:list,path:str):
    with open(path,"w") as file:
        for elemento in lista_personajes:
            file.write("{0},{1},{2}\n".format(elemento["nombre"],elemento["altura"],elemento["fuerza"]))
