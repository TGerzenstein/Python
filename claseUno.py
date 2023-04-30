
"""Este es
mi primer programa"""
"""
saludo = 'Hola mundo!'
print(saludo)

#suma
a = 3
b = 2
suma=a+b
print(suma)
"""

"""
s1 = "Parte 1"
s2 = "Parte 2"
print(s1 + " " + s2)

print(len("Hola, como estas, mucho gusto."))
resultado = 8 * " Hola "
print(resultado)
"""

"""
nombre = input("Ingresa tu nombre: ")
ventas_totales = int( input("Ingresa las ventas totales: ") )
comision = ventas_totales * 6 / 100
print(f"El vendedor {nombre} tiene unas comisiones de ${comision}")"""

#Mensaje de nombre;
"""
nombre = input("Ingresa tu nombre: ")
print(nombre)
"""
#Mensaje de bienvenida;
"""
nombre = input("Ingresa tu nombre: ")
print("¡Bienvenido a python", nombre, "!")
"""

#Mensaje de edad
"""
edad = input("Ingresa tu edad: ")
print("La edad es: ", edad)
"""

#Suma
"""
a = 12
b = 14
suma = a + b
print(suma)
"""

#CocienteyResto


"""
n1 = int(input("Ingrese número: "))
n2 = int(input("Ingrese número: "))
resultado = divmod(n1,n2)
print(f"El cociente es {n1} y el resto {n2}")
"""


#Circulo
"""
import math
print("Ingresa el radio del círculo: ")
radio = float(input())
area = math.pi * (radio * radio)
print("El area del circulo con radio ",radio,"Es: ",area)
"""

#Area de un triangulo 


"""
base = float(input("Ingresa la base del triangulo: "))
altura = float(input("Ingresa la altura del triangulo: "))
area = (base * altura) / 2
print("El area de un triangulo es: ",area)
"""
#Sumar, restar, multiplicar y dividir dos números
"""
n1 = float(input("Ingresa el 1º numero: "))
n2 = float(input("Ingresa el 2º numero: "))
suma = n1 + n2
resta = n1 - n2
multiplicar = n1 * n2
dividir = n1 / n2
print("El resultado de la suma es: ",suma,"\n de la resta: ",resta,"\n de la multiplicación: ",multiplicar,"\n de la división: ",dividir)

"""

#Conversión dólares a euros
"""
precio_dolar = float(input("Ingresa el costo del dolar en euros: "))
dolares = float(input("¿Cuánto desea convertir?: "))
euros = dolares * precio_dolar
print(f"Los {dolares} dólares equivalen a {euros} euros")
"""


#Longitud

"""
palabra = input("Ingresa una palabra: ")
print("La palabra contiene: ",len(palabra))
"""

#Datos de usuario

nombre_completo = input("Ingresa tu nombre y apellido: ")
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura: "))
peso = int(input("Ingresa tu peso actual: "))
direccion = input("Ingresa tu direccion: ")
telefono = int(input("Ingresa tu número de teléfono: "))
print(f"""La información ingresada es la siguiente:
         Nombre completo: {nombre_completo}
         Edad: {edad}
         Estatura: {estatura} cm
         Peso: {peso} kg
         Dirección: {direccion}
         Número de teléfono: {telefono}""")


   