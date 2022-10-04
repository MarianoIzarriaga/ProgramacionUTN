lista = [1,4,3,8,9,7,18,11,3,5,6,9,7,1]

def buscar_minimo(lista_minimo:list)->int:
    minimo = 0
    for i in range(len(lista_minimo)):
        if(lista_minimo[i] < lista_minimo[minimo]):
            minimo = i
    return minimo

def nahuel_sort(lista_a_ordenar:list)-> list:
    lista_duplicada = lista_a_ordenar.copy()
    lista_ordenada = []
    while(len(lista_duplicada) > 0):
        indice_minimo = buscar_minimo(lista_duplicada)
        minimo = lista_duplicada.pop(indice_minimo)   #pop te da el valor,NO el indice
        lista_ordenada.append(minimo)
    return lista_ordenada


def ivan_sort(lista_original:list)-> list:
    lista_duplicada = lista_original.copy()

    for i in range(len(lista_duplicada)):
        if(lista_duplicada[0] > lista_duplicada[i + 1]):
            lista_duplicada[i],lista_duplicada[i+1] = lista_duplicada[i+1],lista_duplicada[i]
        return lista_duplicada

            
#    if(lista_duplicada[0] < lista_duplicada[1]):
#        buffer = lista_duplicada[0]
#       lista_duplicada[0] = lista_duplicada[1]
#        lista_duplicada[1] = buffer
#    return lista_duplicada
        
print(buscar_minimo(lista))
print(nahuel_sort(lista))
