""" 


#lista= [1,2,3,4,5]
#for elemento in lista:
#    print(lista)

#fruta = ["Banana","pera","uva"]
#for x in fruta:
#    print(fruta)

"""
for x in range(0,50,2):  #start dónde arranca #stop dónde comienza #step los saltos que va a hacer
        print(x)     


"""
1_
Crea una calculadora que sea capaz de:
- Solicitar un número al usuario
- Solicitar una operación a realizar
- Solicitar un nuevo número
- Muestre el resultado de la operación entre los dos números
- Asigne el resultado como primer número
- El bucle empieza nuevamente desde pedir orperación
Tener en cuenta: Método de salida del programa, Case sensitive,
las operaciones son solo suma,resta,division,multiplicacion '''

"""

numero1 = float(input("Ingresá un número: "))
numero2 = float(input("Ingresá un nuevo número: "))

while True:
     
     print("""
          Qué op deseas utilizar:
        1) Suma
        2) Resta
        3) Multiplicación
          """)
     op = int(input("Selecciona tu opción: "))
     if op == 1:
        print("La suma es",numero1+numero2)
     elif op == 2:
        print("La resta es",numero1-numero2)
     elif op == 3:
        print("La múltiplicación es",numero1*numero2)
     break
     continue




