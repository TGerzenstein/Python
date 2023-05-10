#Desafío3 = Adivina el número


#Importo la función random
import random
                              
#Definimos nuestras variables:

#Se ingresa el nombre
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Bienvenido/a {nombre}! Deberás adivinar \n un número secreto que está entre el 1 y \n el 100. Solo tienes 8 intentos.") 

#Variable de número de intentos 
num_intentos = 8
#Variable donde se guarda el nº secreto
num_aleatorio = random.randint(1,100)
#Variable "bandera"
ganar = False

#Comienza el juego. Comienza a iterar.
while num_intentos > 0:
  num = input("Ingresa un número: ")
  #Se empleza esta condicion en caso de que se ingrese un número no entero. 
  # Volver a preguntar al usuario, sin descontar intentos.   
  while not num.isdigit():
    print("Ingresa un número entero, por favor.")
    num = input("Vamos... Adivina el número: ")
      
  if int(num) == num_aleatorio:
    print("¡Ganaste! Lo lograste al intento número "+str((8-num_intentos)+1)+".")
    ganar = True
    break

  elif int(num) > num_aleatorio:
    num_intentos = num_intentos - 1
    print("No acertaste. Tu número es mayor. Tenes "+str(num_intentos)+" intentos.")

  else:  
    num_intentos = num_intentos - 1
    print("No acertaste. Tu número es menor. Tenes "+str(num_intentos)+" intentos.")

  #Finalizar
  #En caso de perder el juego, informar el número secreto.
  if num_intentos == 0:
    print("Perdiste! El número secreto era: "+str(num_aleatorio))

  