
#Proyecto para práctica de Programación Orientada a Objetos;

#Concesionaria de Motos

#Se crea la clase Motocicleta

class Motocicleta:
    motor = False
    estado = "nueva"

    #Se crea el método init con los siguientes atributos     
    def __init__(self,color, matricula,combustible_litros,capacidad_maxima_combustible,ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.capacidad_maxima_combustible = capacidad_maxima_combustible
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso

    #Método arrancar
    def arrancar(self):
        if self.motor: 
          print("Arrancó el motor.")
        else: 
          print("El motor ya estaba funcionando.")

    #Método detener
    def detener(self):
        if self.motor:
          print("Se detuvo el motor.")
        else: 
          print("El motor ya estaba detenido.")


    def precio_moto(self):
      return print(f"-> La motocicleta {self.marca} con modelo el {self.modelo} el precio es {self.precio} pesos.")
    

    def informar_combustible(self):
       print(" ")
       print("----- Informar combustible disponible -----")
       print(f"Reporte de la motocicleta de marca {self.marca} con modelo {self.modelo}.")
       print(f"La cantidad disponible de combustible es {self.combustible_litros} litros.")


    def combustible_disponible(self):
        recargado = False
        while recargado != True:
          self.cargar_combustible = float(input("Ingrese la cantidad de combustible que desea cargar: "))
          if self.cargar_combustible + self.combustible_litros <= self.capacidad_maxima_combustible:
            print(f"-> Se cargó {self.cargar_combustible} litros al tanque.")
            self.combustible_litros += self.cargar_combustible
            print(f"El tanque tiene ahora {self.combustible_litros} litros.")
            recargado = True
            break
          else:
             print("La cantidad que deseas cargar supera al límite máximo de la capacidad del tanque.")

print(" ")
print("----------- Primer Objeto -----------")
#Primer instancia de la clase Motocicleta
#Atributos: color, matricula, combustible_litros, capacidad_maxima_combustible, ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso
#Combustible_litros: 10
#Ruedas: 2
moto_uno = Motocicleta("Negra",123,10,17,2,"Honda","RDF-20","23/05/2023",500,2500)
#Prueba del método
moto_uno.arrancar()


#Segunda instancia
print(" ")
print("----------- Segundo Objeto -----------")
moto_dos = Motocicleta(peso = 6000,
                       color = "Gris",
                       modelo = "KLD-23",
                       marca = "BMW",
                       matricula = "RDD-23",
                       combustible_litros = 4,
                       fecha_fabricacion = "12/04/2023",
                       velocidad_punta = 400,
                       ruedas = 2,
                       capacidad_maxima_combustible = 20)
      

#Se añade el atributo "precio", por fuera de la clase
moto_dos.precio = 200000000
print(f"-> La moto {moto_dos.marca} con modelo {moto_dos.modelo} el precio es {moto_dos.precio} pesos.")

#Llamada de los métodos
moto_dos.precio_moto()

#13 - Si intentamos llamar al método con el objeto moto_uno dará error, porque no hay ningun atributo "precio" definido por fuera de la clase; 

#Para saber el reporte del combustible disponible
moto_dos.informar_combustible()


#Método para saber cuánto se carga al tanque
moto_dos.combustible_disponible()

