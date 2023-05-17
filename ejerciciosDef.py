

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
