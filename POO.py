
class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    
    def get_color(self):
        return self.color
        
    def get_ruedas(self):
        return self.ruedas


class Coche(Vehiculo):
    
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def get_velocidad(self):
        self.velocidad

    def get_cilindrada(self):
        self.cilindrada


#mi_vehiculo = Vehiculo('ford','5')
#print(mi_vehiculo)
#mi_coche = Coche('rojo',5,20,233)
#print(mi_coche.get_color())


class Camioneta(Coche):
    
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga = carga

    def get_carga(self):
        return self.carga

    
mi_camioneta = Camioneta('Rojo',4,20,2.5,300)
print(mi_camioneta.get_carga()) 
        



