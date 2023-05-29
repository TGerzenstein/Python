
#Desafío 4: La Inmobiliaria

def menu():
    """Funcion que brinda un menú de opciones para el usuario"""

    print("""
    ¡Bienvenido a la inmobiliaria!
    MENU:
    1 -> Agregar
    2 -> Eliminar
    3 -> Cambiar estado
    4 -> Buscar inmueble según presupuesto y disponibilidad
    0 -> Salir
    """)



#Lista que contiene los inmuebles. A cada inmueble se agregó un ID con un par de clave,valor
lista_pisos = [{'id': 1, 'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
  {'id': 2, 'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
  {'id': 3,'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
  {'id': 4, 'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
  {'id': 5, 'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]



#variable para el bucle while
opcion = -1


#Desarrollo de las funciones:

def agregar_inmueble():
    """Función para agregar a la lista de un inmueble"""  

    print(f"Estos son los inmuebles actuales: \n -> {lista_pisos}")
    print(" ")
    print("Ingrese por favor los datos del inmueble que desea agregar")

    id = int(input("Escribe el ID del inmueble: "))

    anio = int(input("Escribe el año del inmueble: "))
    while anio < 2000:
         anio = int(input("El año debe ser mayor o igual al año 2000. Ingrese el año nuevamente: "))

    metros = int(input("Ingrese los metros que posee el inmueble: "))
    while metros < 60:
          metros = int(input("Los metros deben ser mayor o igual a 60 mts. Ingrese los metros nuevamente: "))    
    
    habitaciones = int(input("Ingrese el número de habitaciones: "))
    while metros < 60:
      metros = int(input("Los metros deben ser mayor o igual a 60 mts. Ingrese los metros nuevamente: "))

    garaje = input("Ingrese S si tiene garaje, o N si no tiene: ").capitalize()
    if garaje == 'S':
      garaje_booleano = True
    else:
      garaje_booleano = False 
    
    zona = input("Ingrese la zona donde está ubicado el inmueble: ")
    while zona not in ['A','B','C']:
       zona = input("La zona debe ser A, B o C. Ingrese la zona nuevamente: ").capitalize()


    estado = input("Ingrese el estado del inmueble: ")
    while estado.lower() not in ['d','r','v']:
      estado = input("El estado debe ser\' d -> Disponible \', \' r -> Reservado \' o \'v -> Vendido \' . Ingrese el estado nuevamente: ")
  
    else:
       
        if estado == 'd':
           estado = 'Disponible'
        elif estado == 'r':
           estado = 'Reservado'
        else:
           estado = 'Vendido'

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
    print(f"Lista actualizada con el índice en la posición {posicion} y su estado {estado} es: \n -> {lista_pisos}")  

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
    print("¡Gracias por utilizar nuestro servicio!")

def ingresar_opcion_correcta():
    print("Por favor, ingrese una de las opciones que aparecen en el menú.")



while opcion != 0:
  menu()
  opcion = int(input("Ingrese la opción que desea realizar: \n-> "))

  if opcion == 1:
    agregar_inmueble()

  elif opcion == 2:
    eliminar_inmueble(lista_pisos)

  elif opcion == 3:
    #Variables
    #Para ingresar a la lista por posición según su índice 
    posicion = int(input("Indique la posición del inmueble a cambiar: ")) 
    #Para ingresar estado que se quiere modificar según las reglas de validación
    estado = input("""Escriba el estado que desea actualizar:                            
                     \n-> Disponible \n-> Reservado \n-> Vendido \n-> """).capitalize()  
    cambiar_inmueble_estado(posicion,estado)

  elif opcion == 4:
    #Llamado de la funcion con los siguientes parámetros: lista y presupuesto
    buscar_piso(lista_pisos, presupuesto = int(input("Ingrese el presupuesto que posee: "))) 

  elif opcion == 0:
    despedida_usuario()

  else:
    ingresar_opcion_correcta()

