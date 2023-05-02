#Desafío 2: Analizador de textos



frase = input("Ingresa una frase o fragmento de tu poeta favorito: ").lower()
letras = input("Ingresa 3 letras que quieras: ").lower()

lista = []
lista.append(letras)


#2) Longitud
print(len(frase))

#3) Cuál es la primera letra y cuál es la última

#4) Mostrar el texto en orden inverso.
texto_invertido = "".join(reversed(frase))
print(texto_invertido)

if "python" in frase:
    print("Esta cadena de caracteres posee la palabra python.")
else: 
    print("No posee la palabra.")


