#Desafio 4: La inmobiliaria

print("\n------------------ Inmuebles de la Inmobiliaria ------------------ \n")

lista_pisos = [{'id': 1, 'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
  {'id': 2, 'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
  {'id': 3,'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
  {'id': 4, 'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
  {'id': 5, 'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


print(f"Estos son los inmuebles actuales: \n -> {lista_pisos}")
print(" ")
print("\n------------------ n1 Agregar ------------------ \n")

def agregar_inmueble():
    """Función para agregar a la lista de un inmueble"""  
    
    print("Ingrese por favor los datos del inmueble que desea agregar: ")
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
    print(f"El nuevo inmueble es: \n -> {nuevo_inmueble}")

    return nuevo_inmueble


agregar_inmueble()

#Este es un ejemplo de dato para ingresar en el input por el usuario, teniendo en cuenta las reglas de validación
# dato = {'d': 6, 'año': 2020, 'metros': 150, 'habitaciones': 2, 'garaje': S, 'zona': 'A', 'estado': 'Disponible'}


print(" ")
print("\n------------------ nº 1 Editar ------------------ \n")

""" 
def editar_inmueble(lista_pisos):
    inmueble = int(input("Escribe el número de ID del inmueble que deseas modificar: "))
    if inmueble not in lista_pisos:
       print("Ese inmueble no está en la lista.")
    else:
       inmueble_modificado = int(input("Escribe el ID del inmueble: "))
       lista_pisos['id'] == inmueble_modificado
       print(f"El inmueble se modificó {inmueble}")

    return inmueble

editar_inmueble(lista_pisos)
 """

print(" ")
print("\n------------------ nº 1 Eliminar ------------------ \n")
print(f"La lista actual de inmuebles: \n -> {lista_pisos}") 

def eliminar_inmueble(lista_pisos):
    """Funcion para eliminar un inmueble a través su ID"""
   
    eliminar = int(input("Escribe el número de ID del inmueble que deseas eliminar: "))
    for i in range(len(lista_pisos)):
      if lista_pisos[i]['id'] == eliminar:
        del lista_pisos[i]                
        break
    print(str(lista_pisos))
    

eliminar_inmueble(lista_pisos)


print(" ")
print("\n------------------ nº 2 Cambiar estado ------------------ \n")

#Lista actualizada
print(" ")
print(f"Esta es la lista actual de los inmuebles: \n -> {lista_pisos}")
print(" ")

def cambiar_inmueble_estado(posicion, estado):
    """Funcion que permite cambiar el estado del inmueble"""
    lista_pisos[posicion]['estado']= estado
    print(estado)  

    return estado

#Variables
# Para ingresar posición según su índice 
posicion = int(input("Indique la posición del inmueble a cambiar: "))
# Para ingresar estado que se quiere modificar según las reglas de validación
estado = input("Escriba el estado que desea actualizar: \n-> Disponible \n-> Reservado \n-> Vendido \n-> ").capitalize()
cambiar_inmueble_estado(posicion, estado)
print(" ")
print(f"Lista actualizada con el índice en la posición {posicion} y su estado {estado} es: \n -> {lista_pisos}.")


print(" ")
print("\n------------------ nº 3 Búsqueda de inmuebles ------------------ \n")


def añadir_precio(piso):
    """Funcion para calcular el precio que tienen los inmuebles según las reglas de precio"""
    precio_total = (piso['metros'] * 100 + piso['habitaciones'] * 500 + int(piso['garaje']) * 1500) * (1 - (2020 - piso['año']) / 100)
    
    if (piso['zona'] == 'A'):
      piso['precio'] = precio_total

    if (piso['zona'] == 'B'):
       precio_total *= 1.5
       piso['precio'] = precio_total

    if (piso['zona'] == 'C'):
       precio_total *= 2
       piso['precio'] = precio_total

    else: 
        ("Incorrecto") 

    return precio_total


def buscar_piso(lista_pisos, presupuesto):
    """Funcion para buscar inmuebles según el presupuesto dado por parámetro."""
    
    nueva_lista = []
    for piso in lista_pisos:
      precio_calculado = añadir_precio(piso)
        
      if ((precio_calculado <= presupuesto) and (piso['estado']== 'Disponible')):         
        nueva_lista.append(piso)


    print(f"Las propiedades son: {nueva_lista}")   

    return precio_calculado


#Llamado de la funcion con los siguientes parámetros: lista y presupuesto
buscar_piso(lista_pisos, presupuesto = int(input("Ingrese el presupuesto: ")))

