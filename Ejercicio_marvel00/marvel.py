from data_stark import lista_personajes
#MAS ALTO
personaje_mas_alto = lista_personajes[0]
altura_maxima = float(personaje_mas_alto["altura"])

for heroe in lista_personajes:
    heroe["altura"] = float(heroe["altura"])
    if(heroe["altura"] > altura_maxima):
        altura_maxima = heroe["altura"]

print("Mas alto: {0} - Nombre: {1}".format(altura_maxima,personaje_mas_alto["nombre"]))

#MAS BAJO

personaje_mas_bajo = lista_personajes[0]
altura_minima = float(personaje_mas_bajo["altura"])

for heroe in lista_personajes:
    heroe["altura"] = float(heroe["altura"])
    if(heroe["altura"] < altura_minima):
        altura_minima = heroe["altura"]

print("Mas bajo: {0} - Nombre: {1}".format(altura_minima,personaje_mas_bajo["nombre"]))

# ALTURA PROMEDIO

cantidad_heroes = 0
acumulador_altura = 0

for heroe in lista_personajes:
    cantidad_heroes = cantidad_heroes + 1
    acumulador_altura = acumulador_altura + heroe["altura"]

print("Promedio: {2} - Cantidad: {0} - acumulador: {1}".format(cantidad_heroes,acumulador_altura,acumulador_altura/cantidad_heroes))


