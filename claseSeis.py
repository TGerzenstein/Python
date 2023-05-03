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

films = []                                                     #comenzar una lista vacía

for i in range(1):                                             #La función range() me permite contrar el num de ciclos 
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
        print("Título: "+"["+p["titulo"]+"]")
        print("Año: "+"["+p["anio"]+"]")
        print("Director: "+"["+p["director"]+"]")
        print("Género: "+"["+p["genero"]+"]")

 """

 
#Vamos a crear un juego! En este juego hay un número secreto(entre 1 y 100)
# Solicitá al usuario que ingrese un número, si adivina, gana! 
# Además el programa deberá indicarle al usuario si el número secreto, 
# en cada iteración, es mayor o menor al ingresado.

#range (fin)
#range (inicio,fin)
#range (inicio, fin, pasos)

#variable = 0                   #variable inic                                 


num = int(input("Escribe el número y adivina si es el secreto: "))

while (num > 1) and (num <100):
      if (num >= 26) and (num <= 100):
         print("El número ingresado es mayor al número secreto")
         num = int(input("Escribe el número y adivina si es el secreto: "))
      elif (num >= 1) and (num <= 24):
         print("El número ingresado es menor al número secreto")
         num = int(input("Escribe el número y adivina si es el secreto: "))
      elif num == 25:
         print("¡Ganaste!")
         break     
else:
   print("Fallaste, intenta de nuevo.")
      