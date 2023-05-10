#Desafío3 = Adivina el número


#Importo la función random
import random
                              
#Definimos nuestras variables:

#Se ingresa el nombre
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Bienvenido/a {nombre}! Deberás adivinar \n el número entre el 1 y el 100. Solo tienes 8 intentos.") 

#Variable de número de intentos 
num_intentos = 8
num_aleatorio = random.randint(1,100)
ganador = False

while num_intentos > 0:
  num = input("Ingresa un número: ")
      
  while not num.isdigit():
    print("Ingresa un número entero, por favor.")
    num = input("Vamos... Adivina el número: ")
      
  if int(num) == num_aleatorio:
    print("¡Ganaste! con el número de ",num_intentos)
    ganador = True
    break

  elif int(num) > num_aleatorio:
    print("Tu número es mayor. Tenes "+str(num_intentos))
    
  else:  
    print("Tu número es menor. Tenes "+str(num_intentos))
  num_intentos= num_intentos - 1

""" 
if num != num_aleatorio:
  num_intentos=str(num_intentos)
  print(f"{nombre} no lo lograste. El número secreto es: {num_aleatorio}") """