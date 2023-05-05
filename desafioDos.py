#Desafío 2: Analizador de textos


#Ingresando los datos
frase = input("Ingresa una frase o fragmento de tu poeta favorito: ").lower()
a = input("Ingresa una letra que vos desees: ").lower()
b = input("Ingresa una letra que vos desees: ").lower()
c = input("Ingresa una letras que vos desees: ").lower()

#Se eliminan signos de puntuación
eliminar = ".;,:¡!¿?\"\'"
for caracter in eliminar:
  frase = frase.replace(caracter, "")

#Se eliminan los espacios
palabras = frase.split()                                        
print(" ")
print("El texto ingresado por el usuario es: \n -->",frase)
print(" ")


#1 - Cantidad de veces que aparecen las letras que elegiste: 
print(f"La cantidad de veces que aparece {a} es: ",frase.count(a))
print(" ")
print(f"La cantidad de veces que aparece {b} es: ",frase.count(b))
print(" ")
print(f"La cantidad de veces que aparece {c} es: ",frase.count(c))
print(" ")

#2 - Mostrar la longitud de palabras en el texto:
print("El número total de palabras es: ", len(palabras))
print(" ")


#3 - Caracteres:
#El primer caracter del texto es: 

primer_letra = palabras[0]
ultima_letra = palabras[-1]


if len(primer_letra) > 0:
  y = primer_letra[0]
  print(f"El primer caracter del texto es: {y}")

if len(ultima_letra) > 0:
  x = ultima_letra[-1]
  print(f"El ultimo caracter del texto es: {x}")
  print(" ")

else:
  print("Por favor, revisa tu opcion")   


#4 -Mostrar en orden inverso de la frase: 
invertir_texto = palabras.copy()
invertir_texto.reverse()                                             
print(f"El texto inverso quedaría así: \n --> {invertir_texto}")
print(" ")


#Encontrar la palabra "python"
encontrado = False

for ele in palabras:
  if ele == "python":
    encontrado = True

if encontrado:
  print("La palabra Python está en el texto.")
    
else:
  print("No está la palabra Python.")
