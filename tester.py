
#Desafío 4: La Inmobiliaria

def menu():
    """Funcion que brinda un menú de opciones para el usuario"""

    print("""
    ¡Bienvenido a la inmobiliaria!
    1 -> Agregar
    2 -> Eliminar
    3 -> Cambiar estado
    4 -> Buscar inmueble
    0 -> Salir
    """)
   
menu()
 

#Lista que contiene los inmuebles. A cada inmueble se agregó un ID con un par de clave,valor
lista_pisos = [{'id': 1, 'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
  {'id': 2, 'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
  {'id': 3,'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
  {'id': 4, 'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
  {'id': 5, 'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


#variable para el ciclo while
opcion = -1

#Desarrollo de las funciones:

def agregar_inmueble():
    """Función para agregar a la lista de un inmueble"""  

    print(f"Estos son los inmuebles actuales: \n -> {lista_pisos}")
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


#Este es un ejemplo de dato para ingresar en el input por el usuario, teniendo en cuenta las reglas de validación
# dato = {'d': 6, 'año': 2020, 'metros': 150, 'habitaciones': 2, 'garaje': S, 'zona': 'A', 'estado': 'Disponible'} 



def eliminar_inmueble(lista_pisos):
    """Funcion para eliminar un inmueble a través su ID"""
    
    print(f"La lista actual de inmuebles: \n -> {lista_pisos}") 
    
    eliminar = int(input("Escribe el número de ID del inmueble que deseas eliminar: "))
    for i in range(len(lista_pisos)):
      if lista_pisos[i]['id'] == eliminar:
        del lista_pisos[i]                
        break
    print(str(lista_pisos))
    


def cambiar_inmueble_estado(posicion, estado):
    """Funcion que permite cambiar el estado del inmueble"""

    lista_pisos[posicion]['estado']= estado
    print(f"Lista actualizada con el índice en la posición {posicion} y su estado {estado} es: \n -> {lista_pisos}.")  

    return estado



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


    print(f"Las propiedades disponibles son: {nueva_lista}")   

    return precio_calculado



def despedida_usuario():
    print("Gracias por utilizar nuestro servicio!")


while opcion != 0:
  opcion = int(input("Ingrese la opción que desea consultar: \n-> "))

  if opcion == 1:
    agregar_inmueble()

  if opcion == 2:
    eliminar_inmueble(lista_pisos)

  if opcion == 3:
    #Variables
    #Para ingresar a la lista por posición según su índice 
    posicion = int(input("Indique la posición del inmueble a cambiar: ")) 
    #Para ingresar estado que se quiere modificar según las reglas de validación
    estado = input("""Escriba el estado que desea actualizar:                            
                     \n-> Disponible \n-> Reservado \n-> Vendido \n-> """).capitalize()  
    cambiar_inmueble_estado(posicion,estado)

  if opcion == 4:
    #Llamado de la funcion con los siguientes parámetros: lista y presupuesto
    buscar_piso(lista_pisos, presupuesto = int(input("Ingrese el presupuesto que posee: "))) 

  if opcion == 0:
    despedida_usuario()
  else:
      ("Su opción es incorrecta.")


