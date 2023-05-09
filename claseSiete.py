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

""" 
#Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes.

Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras,
tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule
el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras.
El precio de venta será 1.5 veces el costo total, que viene determinado por el tamaño,
más el número de ingredientes. En particular el costo total se calcula sumando:
- un costo fijo de preparación.
- un costo variable que es proporcional al tamaño de la pizza.
- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada
ingrediente extra tiene el mismo costo).
"""



#Compra de una pizza. El usuario debe elegir su opción según el tamaño:
pedido = int(input("""¡Bienvenido! Elige tu pizza: 
                  1 - Chica
                  2 - Mediana 
                  3- Grande 
               -->"""))
num_de_ingredientes = int(input("Ingresa el número de ingredientes adicionales: "))
costo_fijo = 1.5


if pedido == 1:
  print("Pediste pizza chica")
  pagar = 1100 + costo_fijo * num_de_ingredientes

elif pedido == 2:
  print("Pediste una pizza mediana")
  pagar = 1200 + costo_fijo * num_de_ingredientes

elif pedido == 3:
  print("Pediste pizza grande")
  pagar = 1300 + costo_fijo * num_de_ingredientes

else:
  print("No pediste nada") 

#Prueba del programa:  
print(f"El número de ingredientes es= {num_de_ingredientes}")
print(f"Tu pedido tiene un costo de: {pagar}")
