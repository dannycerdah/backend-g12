# numero=0
# while numero<=10:
#     print(numero)
#     numero +=1
#     # break
# else:
#     print('el while termino bien')

numeros =[1,5,16,28,234,67,29]

contadorPar=0
contadorImpar=0

for numero in numeros:
    if (numero%2)==0 :
        contadorPar +=1
    else:    
         contadorImpar +=1

 

print('Numeros Pares {}'.format(contadorPar))
print('Numeros Impares {}'.format(contadorImpar))