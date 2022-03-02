# coleccion de datos es una variable que puede almacenar varios valores 
# Listas (List)
#ordenadas y que pueden ser modificadas

nombre = ['Pedro','Luis','Danny','Cesar','Magaly']
combinada =['Eduardo',80,False,15.8,[1,2,3]]
#las listas siempre empiezan en la posicion 0
print(nombre[0])
#cuando hacemos el uso de valores negativos en una lista internamente python le dara la vuelta 
print(nombre[-1])

print(nombre)

#saca el ultimo y lo quita del arreglo 
resultado =nombre.pop()
print(resultado)
print(nombre)

#agrega un item mas al arreglo en la ultima posicion
nombre.append('Juana')

#elimina el contenido de un posicion 
del nombre[0]
print(nombre)

#clear() limpia toda la lista y lo deja vacio
nombre.clear()
print(nombre)

x = combinada[:] # .copy()
y = combinada
#solo imprima >1<3
print(combinada[1:3])

print(combinada[:])

print(id(x))
print(id(combinada))
print(id(y))

# inicio hasta el 2 // del 2 hasta el fin 
print(combinada[:2])
print(combinada[2:])

meses_dscto = ['Enero','Marzo','Julio']
mes = 'Septiembre'
mes2 = 'Enero'

print(mes not in meses_dscto)
print(mes2  in meses_dscto)

seccion_a =['Roxana','Juan']
seccion_b =['Julieta','Martin']

print(seccion_a + seccion_b)


dato = input('Ingresa tu nombre:')
print(dato)

#tuplas
#muy similar a la lista excepcion que no se puede modificar
cursos =('backend','fronted',1,True)

print(cursos)
print(cursos[0])
print(cursos[0:1])

variada = (1,2,3,[4,5,6])

variada[3][0]='Hola'

print(variada)

print(2 in variada)

variada_lista = list(variada)

print(variada_lista)

#Conjuntos (Set)
# se desordenan, #se eliminas una posicion es aleatoria #se agrega a cualquier posicion
estaciones ={'Verano','Otonio','Primavera','Invierno'}
print(estaciones)

print('Invierno' in estaciones)
estaciones.add('Otro')
estacion = estaciones.pop()
print(estacion)

#Diccionarios 
# una coleccion de datos desordenada pero cada elemento obedece a una llave definitiva

persona ={
    'nombre':'Danny',
    'apellido':'Cerda',
    'correo': 'danny.cerda@outlook.com'
}
print(persona['apellido'])
#busco determinada de la llave si no la encuentra no retorna opcion none
print(persona.get('apellidos','No hay no esite'))
print(persona.keys())#solo el nombre de columnas
print(persona.values()) # solo valores
print(persona.items()) # solo valores

persona['edad']=28 
#nombre debe de ser tal cual el nombre pues si no existe lo crea 
persona['nombre']='Ximena'
print(persona)

#eliminar la llave de un diccionario 
persona.pop('apellido')