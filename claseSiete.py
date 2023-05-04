'''
Escribir un programa que almacene una cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. Cuente el número de intentos
realizados por el usuario e imprimalo luego de la bienvenida al ingresar correctamente'''
""" 

var = "abc"
cont = 1

nombre = input("Ingresá tu contraseña: ")

while var != nombre and cont <=3 :
          nombre=input("Ingresá tu contraseña: ") 
          cont=cont+1        
if cont <= 3:
    print("Acceso permitido")
else:
    print("No se puede ingresar.")
print("Ya probaste",cont)
 """

'''5_
Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes.
Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras,
tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule
el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras.
El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño,
más el número de ingredientes. En particular el costo total se calcula sumando:
- un costo fijo de preparación.
- un costo variable que es proporcional al tamaño de la pizza.
- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada
ingrediente extra tiene el mismo costo).'''