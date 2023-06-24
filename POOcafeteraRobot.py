


class Cafetera:
    def __init__(self, capacidad_maxima = 10, cantidad_actual = 3, color = "negra"):
        self.capacidad_maxima = capacidad_maxima
        self.cantidad_actual = cantidad_actual
        self.color = color
    
    def get_capacidad_maxima(self):
        return self.capacidad_maxima
    
    def get_cantidad_actual(self):
        return self.cantidad_actual

    def agregar_cafe(self):
        self.cargar_cafe = int(input("Ingrese los litros: "))
        if self.cargar_cafe + self.cantidad_actual <= self.capacidad_maxima:
            self.cantidad_actual += self.cargar_cafe
            print(f"La cafetera ahora tiene {self.cantidad_actual} litros.")
        else:
          print("La cantidad que desea cargar supera la capacidad de la cafetera.")

    #def vaciar(self):
    #    self.cantidad_actual = 0
    #    print(self.cantidad_actual)

    
    def llenar_cafetera(self):
        self.cantidad_actual = self.capacidad_maxima
        print(self.cantidad_actual)


    def servir_taza(self,capacidad_taza):
        if ( capacidad_taza > self.cantidad_actual):
            print("No alcanza para llenar una taza.")
        else:
            self.cantidad_actual -= capacidad_taza
            print("Se cargo la taza.")



cafe1 = Cafetera()
cafe1.agregar_cafe()
#print(cafe1.cantidad_actual)
#cafe1.vaciar()
#cafe1.llenar_cafetera()
#cafe1.servir_taza(3)
#print(cafe1.get_cantidad_actual())
