import json
import re

def cargar_json(path:str):
    """
    Nos transforma el archivo json en una lista\n
    recibe un path donde se encuentra el archivo json\n
    devuelve los datos en formato lista\n
    """
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    #print(buffer_dict)
    return buffer_dict["results"]

def validar_entero(numero_str:str)->int:
    """
    Verifica si un string es o no un entero y si no lo es lo transforma\n
    recibe una string\n
    devuelve numero entero\n
    """
    resultado = re.match("^[0-9]+$",numero_str)
    if(resultado != None):
        return int(numero_str)
    else:
        False

def buscar_maximo(lista_personajes:list,key:str)->int:
    """
    Busca el elemento con el maximo valor teniendo en cuenta la key que le pasemos\n
    recibe una lista donde buscar\n
    devuelve la posicion donde se encuentra el elemento maximo \n
    """
    maximo = 0
    for i in range (len(lista_personajes)):
       for personaje in lista_personajes:
            dato_parseado = validar_entero(personaje[key])
            if(dato_parseado != False):
                if(lista_personajes[i][key] > lista_personajes[maximo][key]):
                    maximo = i
    return int(maximo)
    #maximo = 0
    #for i in range(len(lista_personajes)):
    #    for personaje in lista_personajes:
    #        personaje["height"] = validar_entero("height")
    #    if(personaje["height"] != False):
    #        if(lista_personajes[i]["height"] > lista_personajes[maximo]["height"]):
    #            maximo = i
    #    print(maximo)

def ordenar(lista_personajes:list,key:str)->list:
    """
    Ordena la lista teniendo en cuenta la key que le pasemos\n
    recibe una lista y una key\n
    devuelve una lista en forma ordenada\n
    """
    lista_duplicada = lista_personajes.copy()
    lista_ordenada = []

    while(len(lista_duplicada) > 0):
        indice_maximo = buscar_maximo(lista_duplicada,key)
        elemento_maximo = lista_duplicada.pop(indice_maximo)
        lista_ordenada.append(elemento_maximo)

    for i in lista_ordenada:
        print(i["name"])
    return lista_ordenada

def buscar(lista_personajes:list):
    """
    Verifica si en el texto que le decimos hay coincidencias con el patron\n
    recibe una lista en la que buscar\n
    devuelve las coincidencias\n
    """
    patron = input("Que desea buscar?")
    for personaje in lista_personajes:
        if(re.search(patron,personaje["name"],re.IGNORECASE)):
            print(personaje["name"])
    return personaje

def exportar_csv(lista_personajes:list,path:str):
    """
    Exporta la lista a un archivo csv\n
    recibe una lista y un path\n
    devuelve un archivo csv con los datos obtenidos\n
    """
    with open(path,"w") as file:
        for elemento in lista_personajes:
            file.write("{0},{1},{2}\n".format(elemento["name"],elemento["height"],elemento["mass"]))