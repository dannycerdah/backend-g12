ingresos =int(input('Ingresa tu sueldo:'))

if(ingresos<250):
    print('Recibe el bono y un balon de gas')   
elif (ingresos<=500 and ingresos>250):
    print('Si recibe el bono')    
elif ingresos>500:
    print('No recibe el bono')       
print('Finalizo el programa')