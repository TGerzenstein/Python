

#Algoritmo ingresar materias
"""
materia1 = input("Ingresa la materia: ")
materia2 = input("Ingresa la siguiente materia: ")
dic = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
if materia1 in dic and materia2 in dic:
    print(f"Su nota en {materia1} es {dic[materia1]} y su nota en {materia2} es {dic[materia2]}")
else:
    print("No curso esas materias.") 
"""

#Capitalize
"""
saludo = input("Ingrese una palabra: ")
print(saludo.capitalize())

"""

#Lower
"""
saludo = input("Ingrese una palabra: ")
print(saludo.lower())
"""

#upper
"""
saludo = input("Ingrese una palabra: ")
print(saludo.upper())

"""

#split
"""
fecha = input("Ingrese una fecha: ").split("-")
print(fecha)

dia,mes,anio = input("Ingrese su fecha: ").split("/")
edad = 2023 - int(anio)
print(f"Día: {dia} Mes: {mes} Año: {anio} Edad: {edad}")

"""


#Listas si se pueden modificar
"""
ejem = ["Hola", "Cómo","Estás","?", 0,12, 10]
ejem[1] = 12
print(ejem)

"""

"""
ejem = ["Hola", "Cómo","Estás","?", 0,12, 10]
print(id(ejem))

"""

#tuplas no se pueden modificar
"""
mensaje = (0, 2, "mensaje", "hola")
print(mensaje.count("mensaje"))

"""

#Diccionarios

#Crear un diccionario con nombres de tres frutas y sus respectivos precios
"""
frutas = {
    "manzana": 910,
    "pera": 1210,
    "ciruela": 2309,
    "banana": 600
}

print(frutas)
"""

#Crear una lista con los nombres de 3 ciudades y agregar una cuarta ciudad al final
"""
ciudades = ["Los Angeles","Amsterdam","Berlín","Londres"]
ciudades.append("Nueva York")
print(ciudades)

"""

#Crear una lista con los nombres de 3 países y mostrar el segundo país de la lista
"""
ciudades = ["Estados Unidos","Uruguay","España"]
print(ciudades[1])

"""

#Crear un diccionario con tres personas y sus respectivas edades
"""
edades = {
    "María": 35,
    "Andrés": 32,
    "Agustín": 33
}

print(edades["Agustín"])
"""


#Crear un set/conjunto con los números del 1 al 10 y mostrar el número más grande en el conjunto
"""

conjunto = {1,2,3,4,5,6,7,8,9,10}
print(max(conjunto))
"""

#Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número de elementos en el conjunto
"""

conjunto = {1,3,5,7,9}
print(len(conjunto))
"""

#Diccionario con los nombres de 3 ciudades y sus respectivas poblaciones. Agregar una cuarta ciudad 

"""
ciudades = {"Los Angeles": 140000,
            "Amsterdam": 10000,
            "Berlín": 12300
        }

key, value = "Madrid", 12000 
ciudades.update({key: value})
print(ciudades)

"""

#Mostrar una lista en orden inverso
"""
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.reverse()
print(numeros)
"""

#Mostrar los países ingresados alfabéticamente
"""
paises = ["Alemania","Colombia","Argentina", "Brasil"]
paises.sort()
print(paises)

"""

#Crear una lista con nombres de 3 frutas y eliminar la segunda fruta
"""
frutas = ["Banana","Pera", "Uvas"]
del frutas[1]
print(frutas)

"""

#Crear una lista con los nombres de tres animales y agregar un cuarto animal al principio
"""
animales = ["Perro","Ave", "Gato", "Elefante"]
animales.insert(0,"Caballo")
print(animales)

"""

#Crear una lista con los nombres de tres países y reemplazar el segundo país de la lista por otro país. Mostrar la lista resultante.
"""
paises = ["Alemania", "Argentina", "Paraguay"]
paises[1] = "Bolivia"
print(paises)

"""

#Crear una lista con los nombres de tres colores y agregar dos colores más al
#final de la lista. Mostrar la lista resultante
"""
colores = ["Verde", "Amarillo", "Rojo"]
colores.append("Azul")
colores.append("Violeta")
print(colores)
"""


# Escribir un programa que guarde en un diccionario los precios de 5 frutas distintas, pregunte al usuario por una fruta, 
#un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
#debe mostrar un mensaje informando de ello
"""
frutas = {
    "manzana": 910,
    "pera": 1210,
    "ciruela": 2309,
    "banana": 600,
    "kiwi": 2000
}
fruta = input("Qué fruta deseas comprar: ")
kilos = float(input("Cuántos kilos de esa fruta: "))
if fruta in frutas:
    print(f"{kilos} kg de {fruta} posee un precio de {frutas[fruta]*kilos} pesos")
else: 
    print("No hay stock de esa fruta.")

"""

#Crear un programa que pregunte al usuario 3 numeros y 
# los guarde en una variable lista, y sume esa lista y 
# muestre al usuario esa suma, tenes la funcion sum() que acepta una lista o tupla de valores enteros y devuelve una suma.

"""
num1 = int(input("Ingrese tu número: "))
num2 = int(input("Ingrese tu número: "))
num3 = int(input("Ingrese tu número: "))
lista = []
lista.append(num1)
lista.append(num2)
lista.append(num3)
resultado = sum(lista)
print(resultado)
"""

#Saber si un alumno aprueba o no un curso, sabiendo que aprobara si su promedio de 3 calificaciones 
# es mayor o igual a 70. Queda desaprobado en caso contrario.

"""
consulta1 = int(input("Ingresa tu primera materia: "))
consulta2 = int(input("Ingresa tu segunda materia: "))
consulta3 = int(input("Ingresa tu tercera materia: "))
promedio = (consulta1+consulta2+consulta3)/3
if promedio >= 70:
    print("Aprobaste.")
else:
    print("Desaprobado.")

"""

#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje: <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.


"""
nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
direccion = input("Escribe tu direccion: ")
telefono = input("Escribe tu teléfono: ")
usuario = {
          "nombre": nombre,
          "edad": edad,
          "direccion": direccion,
          "telefono": telefono
}

print(usuario["nombre"],"tiene",usuario["edad"],"años", "y vive en",usuario["direccion"], "su número de teléfono es", usuario["telefono"])
"""


#Crear algoritmo que cargue 5 numeros y agregar 1 lista. Luego, una vez cargada,
#controle y sustituya cualquier elemento negativo por 0.


#Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud
#máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error

"""
meses = ("Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto", "Septiembre","Octubre","Noviembre","Diciembre")
numeros = int(input("Escribe un número: "))
if (numeros >= 1) and (numeros <= len(meses)):
    print(f"El contenido de esa posición es {meses[numeros-1]}.")
else:
    print("Error.")
"""

#Crea un diccionario que simula ser una Agenda Telefonica y consulta un dato con su clave
"""
agenda = {
          "Manu": 36245789,
          "Juan": 36243356,
          "Andre": 32543625,
          "Maria": 12457113
        }
clave = input("Qué contacto deseas consultar: ").title()
if clave in agenda:
    print(f"Los datos del contacto {clave} es {agenda[clave]}.")
else: 
    print(f"No posees ningún dato de {clave}.")
"""

#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar 5 artículos 
#y sus precios y añadir el par al diccionario. Después se debe mostrar por pantalla la lista de la compra y el monto total

#Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda.
"""
lista1 = ["a","b","c","d","f","g"]
lista2 = ["l","r","s","t","u"]
lista1.extend(lista2)
print("La lista actualizada es: \n",lista1)

"""


#Crear un programa que pida al usuario 2 materias a consultar, 
# el programa debe revisar que esas materias esten dentro de un 
# diccionario calificaciones, las claves de ese diccionario son 
# los nombres de materias y sus valores son un numero calificaciones de ese alumno
"""
clave1 = input("Ingrese la materia a consultar: ").title()
clave2 = input("Ingrese la segunda materia a consultar: ").title()
diccionario = {
               "Matematicas": 10,
               "Literatura": 9,
               "Fisica": 8,
               "Quimica": 9
            }
if (clave1 and clave2) in diccionario:
    print(f"En la materia {clave1} tiene como nota: {diccionario[clave1]}.\n Y en la materia {clave2} tiene como nota: {diccionario[clave2]}.")
else: 
    print("No estas cursando esa materia.")
"""

