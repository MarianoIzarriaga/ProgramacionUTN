'''
1 - Listar TOP N videos
2 - Ordenar videos por duracion (UP/DOWN)
3 - Ordenar videos por cantidad de views (UP/DOWN)
4 - Buscar videos por título 
5 - Exportar lista de videos a CSV
6 - Salir

        {
            "title": "Papa rosti con salchicha parrillera 🥔#paparosti #salchicha #patatas #papa #recetadepapa #shorts",
            "views": 11432,
            "length": 42,
            "img_url": "https://i.ytimg.com/vi/ZGni3XkUEeU/hqdefault.jpg",
            "url": "https://youtube.com/watch?v=ZGni3XkUEeU",
            "date": "2022-09-20 00:00:00"
        }
'''

print("""
1 - Listar TOP N videos
2 - Ordenar videos por duracion (UP/DOWN)
3 - Ordenar videos por cantidad de views (UP/DOWN)
4 - Buscar videos por título 
5 - Exportar lista de videos a CSV
6 - Salir
""")

import func

def paulina_app():
    lista_videos = func.cargar_json(r"C:\Users\maria\Documents\Programacion_UTN\ProgramacionUTN\Ejercicio_paulina\data_paulina_reduce.json")
    while(True):
        respuesta = input()
        if(respuesta == "1"):
            func.listar_videos(lista_videos)
        elif(respuesta == "2"):
            func.ordenar(lista_videos,"length","up")
        elif(respuesta == "3"):
            func.ordenar(lista_videos,"views","down")
        elif(respuesta == "4"):
            func.buscar(lista_videos)
        elif(respuesta == "5"):
            func.exportar_csv(lista_videos,r"C:\Users\maria\Documents\Programacion_UTN\ProgramacionUTN\Ejercicio_paulina\paulina.csv")
        elif(respuesta == "6"):
            print("6 - Salir")
            break
paulina_app()