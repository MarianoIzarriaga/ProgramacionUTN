import json
import re

def cargar_json(path:str)->list:
    with open(path,"r",encoding="utf8") as file:
        buffer_dict = json.load(file)

    return buffer_dict["paulina"]

def validar_entero(numero_str:str)->int:
    result = re.match("^[0-9]+$",numero_str)
    if(result != None):
        return int(numero_str)
    else:
        return False
        
def buscar_minimo(lista_minimo:list,key:str)->int:
    minimo = 0
    for i in range(len(lista_minimo)):
        if(lista_minimo[i][key] < lista_minimo[minimo][key]):
            minimo = i
    return minimo

def buscar_maximo(lista_maximo:list,key:str)->int:
    maximo = 0
    for i in range(len(lista_maximo)):
        if(lista_maximo[i][key] > lista_maximo[maximo][key]):
            maximo = i
    return maximo

def listar_videos(lista_videos:list):
    top = input("\n Cuantos videos desea ver \n")
    top = validar_entero(top)

    if(top != False):
        if(top > len(lista_videos)):
            print("El numero ingresado es invalido")
        else:
            for i in range(top):
                #print(lista_videos[i]["title"],lista_videos[i]["views"])      LAS DOS FORMAS FUNCIONAN
                print("{0} - {1} - {2}".format(lista_videos[i]["views"],lista_videos[i]["length"],lista_videos[i]["title"]))

def ordenar(lista_videos:list,key:str,orden:str)->list:
    lista_duplicada = lista_videos.copy()
    lista_ordenada = []

    while(len(lista_duplicada) > 0):
        if(orden == "down"):
            indice_minimo = buscar_minimo(lista_duplicada,key)
            elemento_minimo = lista_duplicada.pop(indice_minimo)
            lista_ordenada.append(elemento_minimo)
        elif(orden == "up"):
            indice_maximo = buscar_maximo(lista_duplicada,key)
            elemento_maximo = lista_duplicada.pop(indice_maximo)
            lista_ordenada.append(elemento_maximo)

    for video in lista_ordenada:
        print("{0} - {1}".format(video["title"],video[key]))

def buscar(lista_videos:list):
    patron = input("Buscar: ")

    for elemento in lista_videos:
        if(re.search(patron,elemento["title"],re.IGNORECASE)):
            print(elemento["title"])

def exportar_csv(lista_videos:list,path:str):
    with open("path","w") as file:
        for elemento in lista_videos:
            file.write("{0} - {1} - {2}\n".format(elemento["title"],elemento["views"],elemento["length"]))