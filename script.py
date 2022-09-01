flag_barbijo = 0
flag_mas_unidades = 0
acumulador_jabon = 0

for i in range(5):
    tipo = input("Ingrese el tipo ")
    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("Invalido,ingrese otra vez")

    precio = input("Ingrese el precio del producto ")
    precio = int(precio)
    while(precio < 100 and precio > 300):
        precio = input("Invalido,Ingrese el precio otra vez")

    cantidad_unidades = input("Ingrese la cantidad de unidades ")
    cantidad_unidades = int(cantidad_unidades)
    while(cantidad_unidades < 0 and cantidad_unidades > 1000):
        cantidad_unidades = input("Invalido,Ingrese la cantidad otra vez")

    marca = input("Ingrese la marca del producto ")
    fabricante = input("Ingrese el fabricante del producto ")

    if(tipo == "barbijo"):
        if(flag_barbijo == 0):
            flag_barbijo = 1
            barbijo_mas_caro = precio
            unidades_mas_caro = cantidad_unidades
            fabricante_mas_caro = fabricante
        if(precio > barbijo_mas_caro):
            barbijo_mas_caro = precio
            unidades_mas_caro = cantidad_unidades
            fabricante_mas_caro = fabricante       

    if(flag_mas_unidades == 0):
        flag_mas_unidades = 1
        item_mas_unidades = cantidad_unidades
        fabricante_mas_unidades = fabricante
        if(cantidad_unidades > item_mas_unidades):
            item_mas_unidades = cantidad_unidades
            fabricante_mas_unidades = fabricante

    if(tipo == "jabon"):
        acumulador_jabon = acumulador_jabon + cantidad_unidades


    print("El barbijo mas caro es " + barbijo_mas_caro)   
    print("El item con mas unidades es " + item_mas_unidades)  
    print("La cantidad de unidades de jabon es de " + acumulador_jabon)  

