#Desafio 4: La inmobiliaria


def menu():
	print("\n MENU ")
	print(" 1: Agregar inmueble")
	print(" 2: Editar estado de un inmueble ")
	print(" 3: Eliminar inmueble")
	print(" 4: Buscar inmueble según presupuesto y disponibilidad")
	print(" Ingrese cualquier otra tecla para salir: \n")

	return input()


def validarAño(anio):
	while anio < 2000:
		anio = int(input('El año debe ser mayor o igual a 2000. Ingrese año nuevamente: '))

	return (anio)


def validarMetros(metros):
	while metros<60:
		metros = int(input('Los metros deben ser mayor o igual a 60. Ingrese metros nuevamente: '))

	return (metros)


def validarHabit(habit):
	while (habit)<2:
		habit = int(input('La cantidad de habitaciones debe ser mayor o igual a 2. Ingrese habitaciones nuevamente: '))

	return (habit)


def validarZona(zona):
	while zona.upper() not in ['A','B','C']:
		zona = input('La zona debe ser A, B o C. Ingrese zona nuevamente: ')

	return (zona.upper())


def validarEstado(estado):
	while estado.lower() not in ['d','r','v']:
		estado = input('El estado debe ser\'d - Disponible\', \'r - Reservado\' o \'v - Vendido \' . Ingrese estado nuevamente: ')
	else:
		if estado == 'd':
			estado = 'Disponible'
		elif estado == 'r':
			estado = 'Reservado'
		else:
			estado = 'Vendido'


	return (estado)


	
def agregarIn(listaIn):
	inmueble = {}

	print(f'Estos son los inmuebles disponibles {listaIn}\n')

	print('Ingrese datos de inmueble:')

	id = (listaIn[-1]['id'])+1 #obtengo el ultimo id de la lista y lo incremento
	                         # porque el que agrego va a ir al final
	inmueble['id'] = id

	nombre = input('nombre del inmueble: ')
	inmueble['nombre'] = nombre

	anio = int(input('año (debe ser mayor o igual a 2000): '))
	inmueble['año'] = validarAño(anio)
	
	metros = int(input('metros (debe ser mayor o igual a 60): '))
	inmueble['metros'] = validarMetros(metros)

	habit = int(input('cantidad de habitaciones (debe ser mayor o igual a 2) : '))
	inmueble['habitaciones'] = validarHabit(habit)

	garaje = input('Ingrese S si tiene garage, o N si no tiene: ').capitalize()
	if garaje == 'S':
		garaje_booleano = True
	else:
		garaje_booleano = False 
	inmueble['garaje'] = garaje_booleano

	zona = input('zona (A,B o C): ').capitalize()
	inmueble['zona'] = validarZona(zona)

	estado = input('estado--> d-Disponible, r-Reservado, v-Vendido: ')
	inmueble['estado'] = validarEstado(estado)
	
	
	
	listaIn += [inmueble]
	return(listaIn)


def buscarInmueble(id):
	
	for inmueble in listaIn:
		if inmueble['id'] == id:
			return(inmueble)
	

#consideracion cambio de estado: si esta 'Disponible' puede pasar a 'Reservado' 
#si esta 'Vendido' podría volver a estar 'Disponible' si quiere volver a vender el dueño
# si está 'Reservado' puedo pasar 'Disponible' o a 'Vendido'

	
def editarEstadoIn(listaIn): 
	
    print(f'Inmuebles: {listaIn}')
    id = int(input('Ingrese id del inmueble que desea editar: ')) 
    inmueble = buscarInmueble(id)
    print(inmueble)

    if inmueble['estado'] =='Disponible':
      modificacion = input('\n Cambiar estado a \'Reservado\' Y/N?: ')
      if modificacion.lower() in ['y','yes']:
       inmueble['estado'] ='Reservado'  
    
    elif inmueble['estado'] =='Vendido':
      modificacion = input('\nCambiar estado a \'Disponible\' Y/N?:')
      if modificacion.lower() in ['y','yes']:
       inmueble['estado']='Disponible'    
   
    else:
      modificacion = input('\nCambiar estado a d-\'Disponible\',v-\'Vendido\', otra tecla por NO: ')
      
      if modificacion.lower() =='d':
       inmueble['estado'] ='Disponible'
      elif modificacion.lower() =='v':
       inmueble['estado'] ='Vendido'
       print(inmueble)



def eliminar_inmueble(listaIn):
    """Funcion para eliminar un inmueble a través su ID"""
    
    print(f"La lista actual de inmuebles: \n -> {listaIn}") 
    
    id_a_eliminar = int(input("Escribe el número de ID del inmueble que deseas eliminar: "))
    for i in range(len(listaIn)):
      if listaIn[i]['id'] == id_a_eliminar:
        del listaIn[i]                
        break
    print(f'\t\t Inmueble {id_a_eliminar} ELIMINADO \n')
    print(str(listaIn))
    

def añadir_precio(piso):
    """Funcion para calcular el precio que tienen los inmuebles según las reglas de precio"""
    
    if piso['garaje']==True: # convención: si tiene garage se multiplica por 1 al 1500 sino por 0
     cant_garaje = 1
    else:
     cant_garaje = 0

    precio_total = (piso['metros'] * 100 + piso['habitaciones'] * 500 + cant_garaje * 1500) * (1 - (2020 - piso['año']) / 100)
    
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


def buscar_piso(listaIn, presupuesto):
    """Funcion para buscar inmuebles según el presupuesto dado por parámetro."""
    
    nueva_lista = []
    for piso in listaIn:
      precio_calculado = añadir_precio(piso)
        
      if ((precio_calculado <= presupuesto) and (piso['estado']== 'Disponible')):         
        nueva_lista.append(piso)


    print(f"Las propiedades disponibles son: {nueva_lista}")   

    return precio_calculado
 

#Programa

listaIn=[{'id':0, 'nombre': 'Torre Roca','año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'id':1,'nombre': 'Casona Martinez','año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'id':2,'nombre': 'Casa Gloria','año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'id':3,'nombre': 'Edificio Centro','año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'id':4,'nombre': 'Torre A','año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


while True:
	op = menu()
	if op == '1':
		listaIn = agregarIn(listaIn)
		print(listaIn)
	elif op == '2':
		listaIn=editarEstadoIn(listaIn)
	elif op =='3':
		listaIn = eliminar_inmueble(listaIn)
		
	elif op =='4':
		buscar_piso(listaIn, presupuesto = int(input("Ingrese el presupuesto que posee: "))) 
	
	else:
		break

print('Gracias por utilizar nuestro sistema.')
	