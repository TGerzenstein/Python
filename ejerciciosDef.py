

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

def imprimir_pares(num):
  x= 1
  y= num
  while x < y:
    if x % 2 == 0:
      print(x)
    x+=1

imprimir_pares(num=10)



"""for i in range(0,num,2):
    print(i)"""
"""  if num % 2 == 0:
     print(num)
    else:
     print("El num es impar.") """
