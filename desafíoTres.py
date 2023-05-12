#Desafío3 = Adivina el número


#Importo la función random
import random
                              
#Definimos nuestras variables:

#Se ingresa el nombre
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Bienvenido/a {nombre}! Deberás adivinar \n un número secreto que está entre el 1 y \n el 100. Solo tienes 8 intentos.") 

#Variable de número de intentos 
numero_intentos = 8
#Variable donde se guarda el nº secreto
numero_aleatorio = random.randint(1,100)
#Variable "bandera"
es_ganador = False

#Comienza el juego. Comienza a iterar.
while numero_intentos > 0:
  numero = input("Ingresa un número: ")
  #Se emplea esta condicion en caso de que se ingrese un número no entero. 
  # Volver a preguntar al usuario, sin descontar intentos.   
  while not numero.isdigit():
    print("Ingresa un número entero, por favor.")
    numero = input("Vamos... Adivina el número: ")
      
  if int(numero) == numero_aleatorio:
    print("¡Ganaste! Lo lograste al intento número "+str((8-numero_intentos)+1)+".")
    es_ganador = True  
    break

  elif int(numero) > numero_aleatorio:
    numero_intentos = numero_intentos - 1
    print("No acertaste. Tu número es mayor. Tenes "+str(numero_intentos)+" intentos.")

  else:  
    numero_intentos = numero_intentos - 1
    print("No acertaste. Tu número es menor. Tenes "+str(numero_intentos)+" intentos.")

  #Finalizar
  #En caso de perder el juego, informar el número secreto.
  if numero_intentos == 0:
    print("Perdiste! El número secreto era: "+str(numero_aleatorio))

  