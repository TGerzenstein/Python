
""" 
#Funcion cambiar estado del imnueble
def cambiar_valores():
   
    key, value = 'estado', 'Reservado'
 
    lista.update({key: value})
    print(lista)       



cambiar_valores(lista)
 """
""" 
  for ele in lista:
      for clave, valor in ele.items():

       print(clave)
       print(valor)
 """



lista_pisos = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
         {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
         {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
         {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
        {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


lista_pisos[2]['estado']= 'Reservado'
print(lista_pisos)
