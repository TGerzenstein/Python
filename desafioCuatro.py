#Desafio 4: La inmobiliaria

print("\n------------------ Inmuebles ------------------ \n")

lista_pisos = [{'id': 1, 'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
         {'id': 2, 'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
         {'id': 3,'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
         {'id': 4, 'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
        {'id': 5, 'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

 
print("\n------------------ n1 Agregar ------------------ \n")

#Funcion para agregar a la lista un inmueble 
def agregar_inmueble():
        id = int(input("Escribe el ID del inmueble: "))
        anio = int(input("Escribe el año del inmueble: "))    
        metros = int(input("Ingrese los metros del inmueble: "))
        habitaciones = int(input("Ingrese el número de habitaciones: "))
        garaje = input("Ingrese S si tiene garaje, o N si no tiene: ").capitalize()
        zona = input("Ingrese la zona: ")
        estado = input("Ingrese el estado del inmueble: ").capitalize()
        
        if garaje == 'S':
           garaje_booleano = True
        else:
           garaje_booleano = False 

        nuevo_inmueble = {    
          'id': id,                                             
          'año': anio,
          'metros': metros,
          'habitaciones': habitaciones,
          'garaje': garaje_booleano,
          'zona': zona,
          'estado': estado
        }
        lista_pisos.append(nuevo_inmueble)
        print(nuevo_inmueble)

        return nuevo_inmueble


agregar_inmueble()

#Ejemplo de que dato ingresar en el input el usuario
#dato={'d': 6, 'año': 2020, 'metros': 150, 'habitaciones': 2, 'garaje': S, 'zona': 'A', 'estado': 'Disponible'}

print(" ")
print("\n------------------ nº 1 Eliminar ------------------ \n")
 

#Funcion para eliminar el inmueble
def eliminar_inmueble(lista_pisos):
    #lista actualizada
    print(lista_pisos)
    eliminar = int(input("Escribe el número de ID del inmueble que deseas eliminar: "))
    for i in range(len(lista_pisos)):
      if lista_pisos[i]['id'] == eliminar:
        del lista_pisos[i]
        break
    print(str(lista_pisos))
    


eliminar_inmueble(lista_pisos)


print("\n------------------ nº 2 Cambiar estado ------------------ \n")

#Funcion cambiar estado del imnueble
def cambiar_inmueble_estado(posicion, estado):
   
    lista_pisos[posicion]['estado']= estado

    print(lista_pisos)  
    return lista_pisos

posicion = int(input("Indique la posición del inmueble a cambiar: "))
estado = input("Ingrese el estado que desea actualizar: ")
cambiar_inmueble_estado(posicion, estado)


print("\n------------------ nº  ------------------ \n")


def añadir_precio(piso):
    precio_total = (piso['metros'] * 100 + piso['habitaciones'] * 500 + int(piso['garaje']) * 1500) * (1 - (2020 - piso['año']) / 100)
    

    if (piso['zona'] == 'B'):
       precio_total *= 1.5
    
    if (piso['zona'] == 'C'):
       precio_total *= 2

    else: 
        ("Incorrecto") 

    return precio_total



def buscar_piso(lista_pisos, presupuesto):
    
    for i in lista_pisos:
        precio_calculado = añadir_precio(i)
        print(f"El precio es: {precio_calculado}")
        if precio_calculado <= presupuesto:
          print(i)

    
    return precio_calculado

#Poner inputs de presupuesto
print(buscar_piso(lista_pisos, 130000))