#Desafío 2: Analizador de textos


#Ingresando los datos
frase = input("Ingresa una frase o fragmento de tu poeta favorito: ").lower()
a = input("Ingresa una letra que vos desees: ").lower()
b = input("Ingresa una letra que vos desees: ").lower()
c = input("Ingresa una letras que vos desees: ").lower()

#Se eliminan signos de puntuación
eliminar = ".;,:¡!¿?\"\'"
for caracter in eliminar:
    frase  = frase.replace(caracter, "")
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
primer_palabra = palabras[0]

if len(primer_palabra) > 0:
    y = primer_palabra[0]
    print(f'El primer caracter del texto es: {y}')
    print(" ")
else:
    print('Please check.')

#El último caracter del texto es:
ultimo_carac = palabras[-1]

if len(ultimo_carac) > 0:
    x = ultimo_carac[-1]
    print(f'El ultimo caracter del texto es: {x}')
    print(" ")
else:
    print('Please check.')    

#4 -Mostrar en orden inverso de la frase: 
inverso = palabras.copy()
palabras.reverse()                                             
print("El texto inverso quedaría así: \n -->",palabras)
print(" ")

#Encontrar la palabra "python"

