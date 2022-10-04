import json
import re

def cargar_json(path:str)-> list:
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    #print(buffer_dict["pokemones"])
    return buffer_dict["pokemones"]

def validar_entero(numero_str:str)->int:
    result = re.match("^[0-9]+$",numero_str)
    if(result != None):
        return int(numero_str)
    else:
        return False

def listar_pokemones(lista_pokemones:list):
    numero_pokemones = input("Cuantos pokemones desea ver?")
    numero_pokemones = validar_entero(numero_pokemones)

    if(numero_pokemones != False):
        if(numero_pokemones > len(lista_pokemones)):
            print("El numero es invalido")
        else:
            for i in range(numero_pokemones):
                print(lista_pokemones[i])
            return lista_pokemones

def buscar_minimo(lista_pokemones:list,key:str):
    minimo = 0

    for i in range(len(lista_pokemones)):
        if(lista_pokemones[i][key] < lista_pokemones[minimo][key]):
            minimo = i
    return minimo

def buscar_maximo(lista_pokemones:list,key:str):
    maximo = 0

    for i in range(len(lista_pokemones)):
        if(lista_pokemones[i][key] > lista_pokemones[maximo][key]):
            maximo = i
    return maximo

def ordenar(lista_pokemones:list,key:str,orden:str)-> list:
    """
    Ordena la lista de pokemones en la manera que le digamos\n
    recibe una lista a ordenar\n
    devuelve la lista en el orden correspondiente\n
    """
    lista_duplicada = lista_pokemones.copy()
    lista_ordenada = []

    while(len(lista_duplicada) > 0):
        if(orden == "asc"):
            indice_minimo = buscar_minimo(lista_duplicada,key)
            elemento_minimo = lista_duplicada.pop(indice_minimo)
            lista_ordenada.append(elemento_minimo)

        elif(orden == "desc"):
            indice_maximo = buscar_maximo(lista_duplicada,key)
            elemento_maximo = lista_duplicada.pop(indice_maximo)
            lista_ordenada.append(elemento_maximo)
        
    for pokemon in lista_ordenada:
        print(pokemon["nombre"],pokemon[key])
    return lista_ordenada

def calcular_promedio(lista_pokemones:list,key:str,condicion:str):

    acumulador_key = 0
    lista_condicion = []

    for pokemon in lista_pokemones:
        acumulador_key += len(pokemon[key])
    promedio_key = acumulador_key / len(lista_pokemones)

    print(promedio_key)

    for pokemon in lista_pokemones:
        if(condicion == "menor" and len(pokemon[key]) < promedio_key):
            lista_condicion.append(pokemon)
        elif(condicion == "mayor" and len(pokemon[key]) > promedio_key):
            lista_condicion.append(pokemon)

    for pokemon in lista_condicion:
        print(pokemon["nombre"])
    return lista_condicion

def buscar(lista_pokemones:list)->list:
    patron = input("Que desea buscar?")
    lista_patron = []

    for pokemon in lista_pokemones:
        if(re.search(patron,str(pokemon["tipo"]),re.IGNORECASE)):
            print(pokemon["nombre"])
    print(lista_patron)
    return lista_patron

def exportar_csv(lista_pokemones:list,path:str):
    with open(path,"w") as file:
        for pokemon in lista_pokemones:
            file.write("{0},{1},{2},{3},{4},{5}\n".format(pokemon["nombre"],pokemon["tipo"],pokemon["evoluciones"],pokemon["poder"],pokemon["fortaleza"],pokemon["debilidad"]))