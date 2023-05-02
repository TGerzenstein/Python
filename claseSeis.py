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

for i in range(3):                                             #La función range() me permite contrar el num de ciclos 
        titulo = input("Escribe el título de la peli: ")       #bloque del ciclo
        anio = input("Ingrese el año de la peli: ")
        pelicula = {
          "título": titulo,
          "año": anio,
        }
        films.append(pelicula)
    
for clave in range(0,len(films)):
        print(films[clave], end=" ")


