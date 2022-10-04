from data_stark import lista_personajes

def obtener_primer_masculino():
    for heroe in lista_personajes:
        if(heroe["genero"] == "M"):
            return heroe

def obtener_primer_femenino():
    for heroe in lista_personajes:
        if(heroe["genero"] == "F"):
            return heroe

def personajes_hombre():
    for heroe in lista_personajes:
        if(heroe["genero"] == "M"):
            print(heroe["nombre"])

def personajes_mujeres():
    for heroe in lista_personajes:
        if(heroe["genero"] == "F"):
            print(heroe["nombre"])            

def personaje_hombre_mas_alto():
    heroe_mas_alto = obtener_primer_masculino()
    heroe_mas_alto["altura"] = float(heroe_mas_alto["altura"])
    
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if(heroe["altura"] > heroe_mas_alto["altura"]):
            heroe_mas_alto = heroe 
    print("Mas alto: {0} - Nombre: {1}".format(heroe_mas_alto["altura"],heroe_mas_alto["nombre"]))
        
def personaje_femenino_mas_alto():
    heroe_femenino_mas_alto = obtener_primer_femenino()
    heroe_femenino_mas_alto ["altura"] = float(heroe_femenino_mas_alto["altura"])

    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if(heroe["genero"] == "F"):
            if(heroe["altura"] > heroe_femenino_mas_alto["altura"]):
                heroe_femenino_mas_alto = heroe
    print("Mas alto: {0} - Nombre: {1}".format(heroe_femenino_mas_alto["altura"],heroe_femenino_mas_alto["nombre"]))

def personaje_hombre_mas_bajo():
    heroe_masculino_mas_bajo = obtener_primer_masculino()

    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if(heroe["genero"] == "M"):
            if(heroe["altura"] < float(heroe_masculino_mas_bajo["altura"])):
                heroe_masculino_mas_bajo = heroe
    print("Mas bajo: {0} - Nombre: {1}".format(heroe_masculino_mas_bajo["altura"],heroe_masculino_mas_bajo["nombre"]))

def personaje_femenino_mas_bajo():
    heroe_femenino_mas_bajo = obtener_primer_femenino()

    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if(heroe["genero"] == "F"):
            if(heroe["altura"] < float(heroe_femenino_mas_bajo["altura"])):
                heroe_femenino_mas_bajo = heroe
    print("Mas bajo: {0} - Nombre: {1}".format(heroe_femenino_mas_bajo["altura"],heroe_femenino_mas_bajo["nombre"]))

def altura_promedio_masculino():
    cantidad_heroes = 0
    acumulador_altura = 0
    for heroe in lista_personajes:
        if(heroe["genero"] == "M"):
            cantidad_heroes = cantidad_heroes + 1
            acumulador_altura = acumulador_altura + float(heroe["altura"])

    print("Promedio: {2} - Cantidad: {0} - Acumulador: {1}".format(cantidad_heroes,acumulador_altura,acumulador_altura/cantidad_heroes))

def altura_promedio_femenino():
    cantidad_femenino = 0
    acumulador_altura_femenino = 0
    for heroe in lista_personajes:
        if(heroe["genero"] == "F"):
            cantidad_femenino = cantidad_femenino + 1
            acumulador_altura_femenino = acumulador_altura_femenino + float(heroe["altura"])
    print("Promedio: {2} - Cantidad: {0} - Acumulador: {1}".format(cantidad_femenino,acumulador_altura_femenino,acumulador_altura_femenino/cantidad_femenino))

def calcular_cantidad_color_ojos():
    #J-Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    cantidad_color_ojos = {}
    
    for personaje in lista_personajes:
        color_ojos_normalizado = personaje["color_ojos"].lower()
        cantidad_color_ojos[color_ojos_normalizado] = 0

    for personaje in lista_personajes:
        color_ojos_normalizado = personaje["color_ojos"].lower()
        cantidad_color_ojos[color_ojos_normalizado] +=1

    print(cantidad_color_ojos)

def calcular_cantidad_color_pelo():

    cantidad_color_pelo = {}

    for personaje in lista_personajes:
        color_pelo_normalizado = personaje["color_pelo"].lower()
        cantidad_color_pelo[color_pelo_normalizado] = 0
    
    for personaje in lista_personajes:
        color_pelo_normalizado = personaje["color_pelo"].lower()
        cantidad_color_pelo[color_pelo_normalizado] +=1
    
    print(cantidad_color_pelo)

def calcular_cantidad_tipo_inteligencia():
    cantidad_tipo_inteligencia = {}

    for personaje in lista_personajes:
        tipo_inteligencia_normalizado = personaje["inteligencia"].lower()
        cantidad_tipo_inteligencia[tipo_inteligencia_normalizado] = 0
    
    for personaje in lista_personajes:
        tipo_inteligencia_normalizado = personaje["inteligencia"].lower()
        cantidad_tipo_inteligencia[tipo_inteligencia_normalizado] +=1
    
    print(cantidad_tipo_inteligencia)

def agrupar_color_ojos():

    dict_color_ojos = {}

    for personaje in lista_personajes:
        color_ojos_normalizado = personaje["color_ojos"].lower()
        dict_color_ojos[color_ojos_normalizado] = []
    
    for personaje in lista_personajes:
        for color in dict_color_ojos:
            color_normalizado = color.lower()
            if (personaje["color_ojos"].lower() == color_normalizado):
                dict_color_ojos[color_normalizado].append(personaje["nombre"])
    print(dict_color_ojos)

while True:
    respuesta= input(" 1-Nombre heroes hombre \n 2-Nombre heroes mujeres \n 3- Nombre Hombre mas alto \n 4- Nombre Heroe femenina mas alta \n 5- Heroe mas bajo \n 6- Personaje Femenino mas bajo \n 7- Promedio de Altura Masculino \n 8-Promedio de altura Femenino \n9-Agrupar por color de ojos \n10-Agrupar por color de pelo \n11-Agrupar segun tipo de inteligencia")
    if(respuesta == "1"):
        personajes_hombre()
    elif(respuesta == "2"):
        personajes_mujeres()
    elif(respuesta == "3"):
        personaje_hombre_mas_alto()
    elif(respuesta == "4"):
        personaje_femenino_mas_alto()
    elif(respuesta == "5"):
        personaje_hombre_mas_bajo()
    elif(respuesta == "6"):
        personaje_femenino_mas_bajo()
    elif(respuesta == "7"):
        altura_promedio_masculino()
    elif(respuesta == "8"):
        altura_promedio_femenino()
    elif(respuesta == "9"):
        calcular_cantidad_color_ojos()
    elif(respuesta == "10"):
        calcular_cantidad_color_pelo()
    elif(respuesta == "11"):
        calcular_cantidad_tipo_inteligencia()
    elif(respuesta == "12"):
        agrupar_color_ojos()