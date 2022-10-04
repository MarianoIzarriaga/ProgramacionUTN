import json

url = r"C:\Users\maria\Documents\Programacion_UTN\ProgramacionUTN\Ejercicio_marvel04\data_stark.json"
def parse_json(nombre_archivo:str):
    dic_heroes = {}
    with open(nombre_archivo,"r") as archivo:
        dic_heroes = json.load(archivo)
    return dic_heroes["heroes"]

def imprimir_menu_desafio_5():
    mensaje = ("A-Nombre heroes hombre \nB-Nombre heroes mujeres \nC- Nombre Hombre mas alto \nD- Nombre Heroe femenina mas alta \nE-Heroe mas bajo \nF-Personaje Femenino mas bajo \nG-Promedio de Altura Masculino \nH-Promedio de altura Femenino \nI-Informar el nombre de los anteriores \nJ-Agrupar por color de ojos \nK-Agrupar por color de pelo \nL-Agrupar por tipo de inteligencia \nM-Listar por color de ojos \nN-Listar por color de pelo \nO-Agrupar por tipo de inteligencia ")
    print(mensaje)

def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    

print(parse_json(url))
imprimir_menu_desafio_5()