
#Ejercicios práctica de la semana 3

""" 
x = 0

while x < 50:
    print("El valor de x es: ",x)
    x += 1
 """

#1) Escribe un programa que pida al usuario una palabra y luego imprima cada
#letra de la palabra en una línea separada.

""" 
palabra = input("Escribe una palabra: ")

for letra in palabra:
    palabra.split(" ") # separar línea en palabras, por espacio en blanco
    print(letra)
 """

#2) Escribe un programa que imprima los números pares del 1 al 100

""" 
e = 1

while e <= 100:
    if e % 2 == 0:
      print(f"{e} es número es par.")
    e = e + 1  
    
"""

#3) Escribe un programa que pida al usuario una palabra y luego imprima la misma palabra pero con las letras en orden inverso

""" 
palabra = input("Escribe la palabra: ")

for letra in range(len(palabra)-1,-1,-1):
        print(palabra[letra])

"""      

#4) Escribe un programa que pida al usuario una cadena de texto y luego imprima
#el número de palabras que contiene
""" 
texto = input("Escribe un texto: ")
palabras = texto.split()           #dividir
count = 0

for i in palabras:
        count+=1
        print(count)
 """

#Escribe un programa que pida al usuario una cadena de texto y determine
#cuántas veces aparece cada letra en la cadena


"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA,
deberá aplicar un 21%.
"""
