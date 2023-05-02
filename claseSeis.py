"""
Ejercicio: Crea una lista de diccionarios que contenga información consultada a los usuarios 
sobre diferentes películas. 
Cada diccionario debe contener las siguientes claves: "título", "año", "director" y "género". 
Crea al menos 5 diccionarios en la lista.
Después, escribe un programa que recorra la lista y muestre la información de cada película 
en la consola en el siguiente formato:

Título: [título de la película]
Año: [año de la película]
Director: [nombre del director]
Género: [género de la película]

"""


films = []                                                     #comenzar una lista vacía

for i in range(5):                                             #La función range() me permite contrar el num de ciclos 
        titulo = input("Escribe el título de la peli: ")       #bloque del ciclo
        anio = input("Ingrese el año de la peli: ")
        director = input("Ingrese el nombre del director: ")
        genero = input("Ingrese el género de la peli: ")
        pelicula = {                                           
          "titulo": titulo,
          "anio": anio,
          "director": director,
          "genero": genero,
        }
        films.append(pelicula)
    
for p in films:
        print("---------------")
        print("Título:","[",p["titulo"],"]")
        print("Año:","[",p["anio"],"]")
        print("Director:","[",p["director"],"]")
        print("Género:","[",p["genero"],"]")


        
