#Algoritmo para saber si es menor o mayor de edad
"""
edad = int(input("Escribe tu edad:"))
if edad >= 18:
   print("Sos mayor de edad.") 
else:
   print("Sos menor de edad.")
"""


#Ingresar dos números y mostrar cuál de ellos es mayor
"""
a = int(input("Ingresa el primer número: ")) 
b = int(input("Ingresa el segundo número: "))
if a > b:
       print(f'El número {a} es mayor que {b}.')
elif a < b:
       print(f'El número {b} es menor que {a}.')
else:
       print('Es el mismo número.')
"""


#Saber cuál de los números es par e impar
"""
n = int(input("Ingresa el primer número: ")) 
if n % 2 == 0:
   print("El número es par")
else:
   print("El número es impar")
"""

#Ingresar una nota y ver si está aprobado (5 o más) o no
"""
nota = int(input("Ingresa la nota de tu examen: "))
if nota >= 5:
    print("Aprobaste el examen.¡Felicitaciones!")
else:
    print("Desaprobaste el examen.")
"""

"""
cadena_de_caracteres = str(input("Ingrese su cadena de caracteres: "))
if "a" in cadena_de_caracteres:
    print("Esta cadena de caracteres posee la letra a.")
else: 
    print("No posee la letra a.")
"""


"""
#Ingresar una cadena de caracteres y mostrar por pantalla si tiene la letra "a"

cadena_de_caracteres = str(input("Ingrese su cadena de caracteres: "))
if cadena_de_caracteres.find("a") != -1:
    print("Esta cadena de caracteres posee la letra a.")
else: 
    print("No posee la letra a.")

"""
#Ingresar 3 números y mostrar por pantalla el mayor de ellos
"""
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))
if n1 > n2 and n1 > n3:
    print(f"El número {n1} es mayor que {n2} y {n3}.")
elif n2 > n1 and n2 > n3:
    print(f"El número {n2} es mayor que {n1} y {n3}.")
elif n3 > n1 and n3 > n2:
    print(f"El número {n3} es mayor que {n1} y {n2}.")
else: 
    print("Ingresa tres números distintos.")

"""


#Ingresar dos números y muestre por pantalla la suma de ellos solo si ambos son pares
"""
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 % 2 == 0 and num2 % 2 == 0:
      suma = num1 + num2
      print(f"La suma entre los números pares {num1} y {num2}, da como resultado: {suma}.")
else:
   print("Los números ingresados son impares.")

"""

materia1 = ("Ingresa la materia: ")
materia2 = ("Ingresa la siguiente materia: ")
dic = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
if materia1 in dic and materia2 in dic:
    print(f"Su nota en {materia1} es {dic[materia1]} y su nota en {materia2} es {dic[materia2]}")
else:
    print("No curso esas materias.") 