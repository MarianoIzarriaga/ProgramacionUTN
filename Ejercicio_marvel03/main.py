from data_stark import lista_personajes
"""
Crear la función "extraer_iniciales" que recibirá como parámetro: 
nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con las iniciales del nombre del personaje seguidos por un punto (.)
En el caso que el nombre del personaje contenga el artículo "the" se deberá omitir de las iniciales
Se deberá verificar si el nombre contiene un guión "-" y sólo en el caso que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
Que el string recibido no se encuentre vacío
Devolver N/A en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D.

"""
def extraer_inciales(nombre_heroe: str):

    aux_return = "N/A"
    if(type(nombre_heroe) == type(str()) and len(nombre_heroe) > 0):
        nombre_heroe = nombre_heroe.upper()
        nombre_heroe = nombre_heroe.replace("THE ","")
        nombre_heroe = nombre_heroe.replace("-"," ")
        nombre_heroe = nombre_heroe.strip()
        nombre_heroe = nombre_heroe.upper()
        partes_nombre = nombre_heroe.split(" ")

        iniciales = ""
        for parte in partes_nombre:
            iniciales += parte[0] +"."

        aux_return = iniciales
    return aux_return
    #print(partes_nombre)


def definir_iniciales_nombre(heroe:dict):
    aux_return = False
    if(type(heroe) == type(dict())):
        for clave in heroe:
            if(clave == "nombre"):
                heroe["Iniciales"] = extraer_inciales(heroe["nombre"])
                aux_return = True
                break

    print(heroe)
    return aux_return            


def agregar_iniciales_nombre(lista_heroes:list):
    if(type(lista_heroes) == type(list()) and len(lista_heroes) > 0):
        



for heroe in lista_personajes:
    print(extraer_inciales(heroe["nombre"]))
for heroe in lista_personajes:
    definir_iniciales_nombre(heroe)