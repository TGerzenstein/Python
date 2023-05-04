#Desafío 2: Analizador de textos



lista_letras = []

#Generando la frase
frase = input("Ingresa una frase o fragmento de tu poeta favorito: ").lower()
letras = input("Ingresa tres letras que vos desees: ").lower()


#El texto ingresado
print("El texto ingresado por el usuario es: \n -->",frase)
palabras = frase.split()                                        #separar y convertir en lista


#Mostrar la longitud de la lista de palabras:
print("El número total de palabras es: ", len(palabras))

#Mostrar en orden inverso la frase: 
inverso = palabras.copy()
palabras.reverse()                                              #Mostrar el texto en orden inverso 
print("El texto inverso quedaría así: \n -->",palabras)

#Las letras escogidas
print("Las letras escogidas son",letras)

#Guardar en una lista las letras elegidas
letras.append(lista_letras)
#Mostrar
print(lista_letras)


