#Desafio 4: La inmobiliaria


lista_pisos = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'}, 
         {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'}, 
         {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}, 
         {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
        {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


#Funcion agregar inmueble 
def agregar_inmueble(dato):
    lista_pisos.append(dato)
    print(lista_pisos)


    return lista_pisos


dato={'año': 2020, 'metros': 150, 'habitaciones': 2, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}
agregar_inmueble(dato)
print("\n------------------ nº  ------------------ \n")


#Funcion eliminar inmueble
def eliminar_inmueble(dato):
    lista_pisos.remove(dato)
    print(lista_pisos)

    return lista_pisos


eliminar_inmueble(dato)
print("\n------------------ nº  ------------------ \n")


#Funcion cambiar estado del imnueble
def cambiar_valor(lista_pisos):
    
    lista_pisos[2]['estado']= 'Reservado'

    print(lista_pisos)  
    return lista_pisos


cambiar_valor(lista_pisos)
print("\n------------------ nº  ------------------ \n")


# Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
# Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
# Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2

def añadir_precio(piso):
    zona = (piso['metros'] * 100 + piso['habitaciones'] * 500 + int(piso['garaje']) * 1500) * (1 - (2020 - piso['año']) / 100)
    
    if (piso['zona'] == 'A'):
     piso['precio'] = zona

    if (piso['zona'] == 'B'):
     zona *= 1.5
     piso['precio'] = zona
    
    if (piso['zona'] == 'C'):
     zona *= 2
     piso['precio'] = zona
    else: 
         None

    return piso


def buscar_piso(lista_pisos, presupuesto):
    def filtrar(piso):
        return piso['precio'] <= presupuesto

    return list(filter(filtrar,map(añadir_precio, lista_pisos)))


print(buscar_piso(lista_pisos, 100000000))