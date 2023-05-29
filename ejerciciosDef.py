

#Crea una función llamada suma que tome dos números como parámetros y
#devuelva la suma de ellos

""" 
def suma(num1,num2):
    resultado = num1 + num2
    print(resultado)
    #return resultado

suma(42,42)
"""


#Crea una función llamada saludo que tome el nombre de una persona como
#parámetro e imprima un saludo personalizado.

""" 
def saludar(nombre):
    print(nombre)
    return nombre


saludar(nombre="Andres")
saludar(nombre="Marcos")

 """


#Crea una función llamada invertir_cadena que tome una cadena de texto como
#parámetro y devuelva la cadena invertida.

""" 
def invertir_cadena(cadena_de_texto):
    t = ''  
    for ele in cadena_de_texto:
      t = ele + t
      
    print(t)
    return t 

invertir_cadena(cadena_de_texto="Ingrese el texto: ")

"""


#Crea una función llamada es_par que tome un número como parámetro y
#devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
#devuelva Es impar o No es par.


""" 
def es_par(num1):
    
  if num1 % 2 == 0:
    print("El número es par")
  else:
    print("El número es impar")
  

es_par(num1=int(input("Ingresa el primer número: "))) 
 """


#Crea una función llamada imprimir_pares que tome un número entero como
#parámetro y imprima todos los números pares desde 1 hasta ese número.

""" 
def imprimir_pares(num):
  x= 1
  y= num
  while x < y:
    if x % 2 == 0:
      print(x)
    x+=1

imprimir_pares(num=10)
 """


#Crea una función llamada contar_vocales que tome una cadena de texto como
#parámetro y devuelva el número de vocales que contiene.
""" 
def contar_vocales(cadena_texto):
    Cuenta las vocales que hay en una cadena de texto
    
    vocales = "aeiou"
    contador = 0
    for i in cadena_texto:
        if i in vocales:
          contador = contador + 1
    
    print(f"Esta frase tiene {contador} vocales")
    
contar_vocales(cadena_texto="Hola mundo")

"""


#Crea una función llamada convertir_temperatura que tome una temperatura
#en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
#es: Fahrenheit = (Celsius * 9/5) + 32


""" 
def convertir_temperatura(celcius):
     Convierte grados Celcius en grados Fahrenheit 
    
    return (celcius * 9/5) + 32
    

print(convertir_temperatura(celcius = 14))
 """


#Definir una función que calcule la longitud de una lista
#o una cadena dada. No tenemos que usar el método len()
""" 

def contar_longitud(cadena):
   #Cuenta las vocales que hay en una cadena de texto
    
  contador = 0
  for i in cadena:
      contador = contador + 1
    
  print(f"Esta frase tiene {contador} letras")
    
contar_longitud(cadena="Hola mundo")
"""



#Definir una función max_de_tres(), que tome tres números
#como argumentos y devuelva el mayor de ellos. Sin math.max() y ningún método.

""" 
def max_de_tres(numero1,numero2,numero3):
   if numero1 > numero2:
      print(f"{numero1} es mayor.")
   elif numero2 > numero3:
      print(f"{numero2} es mayor.")
   else: 
      print(f"{numero3} es mayor.")


max_de_tres(123,144,1000)

"""


#Escribir una función suma() y una función multiplicacion() que sumen y
#multipliquen respectivamente todos los números de una lista. 


def sumar(lista):
   suma = 0
   
   for elemento in lista:
      suma = suma + elemento
   print(suma)

   return suma  



def multiplicar(lista):
  producto = 1
  for elemento in lista:
    producto = producto * elemento
  
  print(producto)

  return producto


lista = [1,2,3,45,79]

sumar(lista)
multiplicar(lista)



#Desafio 4: La inmobiliaria

print("\n------------------ Inmuebles de la Inmobiliaria ------------------ \n")

lista_pisos = [{'id': 1, 'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
  {'id': 2, 'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
  {'id': 3,'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
  {'id': 4, 'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
  {'id': 5, 'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


print(f"Estos son los inmuebles actuales: \n -> {lista_pisos}")
print(" ")
print("\n------------------ n1 Agregar ------------------ \n")

def agregar_inmueble():
    """Función para agregar a la lista de un inmueble"""  
    
    print("Ingrese por favor los datos del inmueble que desea agregar: ")
    id = int(input("Escribe el ID del inmueble: "))
    anio = int(input("Escribe el año del inmueble: "))    
    metros = int(input("Ingrese los metros del inmueble: "))
    habitaciones = int(input("Ingrese el número de habitaciones: "))
    garaje = input("Ingrese S si tiene garaje, o N si no tiene: ").capitalize()
    zona = input("Ingrese la zona: ")
    estado = input("Ingrese el estado del inmueble: ").capitalize()
        
    if garaje == 'S':
      garaje_booleano = True
    else:
      garaje_booleano = False 

    nuevo_inmueble = {    
        'id': id,                                             
        'año': anio,
        'metros': metros,
        'habitaciones': habitaciones,
        'garaje': garaje_booleano,
        'zona': zona,
        'estado': estado
        }
    lista_pisos.append(nuevo_inmueble)
    print(f"El nuevo inmueble es: \n -> {nuevo_inmueble}")

    return nuevo_inmueble


agregar_inmueble()

#Este es un ejemplo de dato para ingresar en el input por el usuario, teniendo en cuenta las reglas de validación
# dato = {'d': 6, 'año': 2020, 'metros': 150, 'habitaciones': 2, 'garaje': S, 'zona': 'A', 'estado': 'Disponible'}


print(" ")
print("\n------------------ nº 1 Eliminar ------------------ \n")
print(f"La lista actual de inmuebles: \n -> {lista_pisos}") 

def eliminar_inmueble(lista_pisos):
    """Funcion para eliminar un inmueble a través su ID"""
   
    eliminar = int(input("Escribe el número de ID del inmueble que deseas eliminar: "))
    for i in range(len(lista_pisos)):
      if lista_pisos[i]['id'] == eliminar:
        del lista_pisos[i]                
        break
    print(str(lista_pisos))
    

eliminar_inmueble(lista_pisos)


print(" ")
print("\n------------------ nº 2 Cambiar estado ------------------ \n")

#Lista actualizada
print(" ")
print(f"Esta es la lista actual de los inmuebles: \n -> {lista_pisos}")
print(" ")

def cambiar_inmueble_estado(posicion, estado):
    """Funcion que permite cambiar el estado del inmueble"""
    lista_pisos[posicion]['estado']= estado
    print(estado)  

    return estado

#Variables
# Para ingresar posición según su índice 
posicion = int(input("Indique la posición del inmueble a cambiar: "))
# Para ingresar estado que se quiere modificar según las reglas de validación
estado = input("Escriba el estado que desea actualizar: \n-> Disponible \n-> Reservado \n-> Vendido \n-> ").capitalize()
cambiar_inmueble_estado(posicion, estado)
print(" ")
print(f"Lista actualizada con el índice en la posición {posicion} y su estado {estado} es: \n -> {lista_pisos}.")


print(" ")
print("\n------------------ nº 3 Búsqueda de inmuebles ------------------ \n")


def añadir_precio(piso):
    """Funcion para calcular el precio que tienen los inmuebles según las reglas de precio"""
    precio_total = (piso['metros'] * 100 + piso['habitaciones'] * 500 + int(piso['garaje']) * 1500) * (1 - (2020 - piso['año']) / 100)
    
    if (piso['zona'] == 'A'):
      piso['precio'] = precio_total

    if (piso['zona'] == 'B'):
       precio_total *= 1.5
       piso['precio'] = precio_total

    if (piso['zona'] == 'C'):
       precio_total *= 2
       piso['precio'] = precio_total

    else: 
        ("Incorrecto") 

    return precio_total


def buscar_piso(lista_pisos, presupuesto):
    """Funcion para buscar inmuebles según el presupuesto dado por parámetro."""
    
    nueva_lista = []
    for piso in lista_pisos:
      precio_calculado = añadir_precio(piso)
        
      if ((precio_calculado <= presupuesto) and (piso['estado']== 'Disponible')):         
        nueva_lista.append(piso)


    print(f"Las propiedades son: {nueva_lista}")   

    return precio_calculado


#Llamado de la funcion con los siguientes parámetros: lista y presupuesto
buscar_piso(lista_pisos, presupuesto = int(input("Ingrese el presupuesto: ")))

