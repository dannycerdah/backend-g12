# notas =[10,20,16,8,6,1]

# for nota in notas:
#     print(nota) 

# for numero in range(10):
#     print(numero)    

# for numero in range(5,10):
#     print(numero)        

# for numero in range(5,10,2):
#     print(numero)       

# notas =[10,20,16,8,6,1]

# print(notas[:3])
from itertools import product


aprobados =['Eduardo','Maria','Pedro','Fatima']

for aprobado in aprobados:
    if(aprobado=='Jhonatan'):
        print('Pedro esta aprobado')
        break 
else:
    print('No se encontro el alumno a buscar')

print('Termino de ejecutarse el for')

productos = ['Manzanas','Peras','Tallarines','Tazas']

busqueda = input('Ingrese el producto a buscar: ')

for producto in productos:
    if producto== busqueda:
        print('El producto si esta en la tienda')
        break
else:
    print('No se encontro el producto')
print('Igual yo me ejecuto')    

