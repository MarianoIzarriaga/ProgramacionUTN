from data_stark import lista_personajes

def stark_normalizar_datos(lista:list):

    for personaje in lista_personajes:
        if(type(personaje["altura"]) == type("")):
            personaje["altura"] = float(personaje["altura"])
        if(type(personaje["peso"]) == type("")):
            personaje["peso"] = float(personaje["peso"])
        if(type(personaje["fuerza"]) == type("")):
            personaje["fuerza"] = int(personaje["fuerza"])



stark_normalizar_datos(lista_personajes)

print(lista_personajes)