

class Vehiculo:
    def __init__(self,marca,ruedas):
        self.marca = marca
        self.ruedas = ruedas

    def __str__(self):
        return "El vehiculo de {} tiene {} ruedas".format(self.marca,self.ruedas)

class Coche:
    def __init__(self,marca,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,marca,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) +" con {} km y {}cc".format(self.velocidad,self.cilindrada)


#mi_vehiculo = Vehiculo('ford','5')
#print(mi_vehiculo)
mi_coche = Coche('ford','5','20','233')
print(mi_coche)