#Desafío 2: Analizador de textos


#Ingresando los datos
frase = input("Ingresa una frase o fragmento de tu poeta favorito: ").lower()
a = input("Ingresa una letra que vos desees: ").lower()
b = input("Ingresa una letra que vos desees: ").lower()
c = input("Ingresa una letras que vos desees: ").lower()



eliminar = ".;,:¡!¿?\"\'"
for caracter in eliminar:
    frase  = frase.replace(caracter, "")

palabras = frase.split()                                        #separar y convertir en lista
print("El texto ingresado por el usuario es: \n -->",frase)

#2 - Mostrar la longitud de la lista de palabras:
print("El número total de palabras es: ", len(palabras))


#Las letras escogidas
print(f"Las letras escogidas son: {a}{b}{c}")



#Guardar en una lista las letras elegidas
lista_letras = []
lista_letras.append(a)
lista_letras.append(b)
lista_letras.append(c)

#3 - Caracteres:
#El primer caracter del texto es: 
name = palabras[0]

if len(name) > 0:
    firstChar = name[0]
    print(f'El primer caracter del texto es: {firstChar}')
else:
    print('Please check.')

#El último caracter del texto es:
last = palabras[-1]

if len(last) > 0:
    lastChar = last[-1]
    print(f'El ultimo caracter del texto es: {lastChar}')
else:
    print('Please check.')    

#4 -Mostrar en orden inverso la frase: 
inverso = palabras.copy()
palabras.reverse()                                             
print("El texto inverso quedaría así: \n -->",palabras)
