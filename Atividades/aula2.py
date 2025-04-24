import numpy as dsa
'''Minupulação array teste'''
#                 0 1 2 3 4 5 6 7 8 9  10 11 12 13 
arr1 = dsa.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

#imprimindo ate
print ('===============================================')

print ("Imprimir até o 4",arr1[:4])
print ('===============================================')

indices = [1,3,5,6,7]
print (arr1 [indices]) #imprime o indice colocado
print ('===============================================')
divide2 = (arr1 %2 == 0) # cada elemento do array é divido ´pr 2
print ("Divisão de itens",divide2) #DEVOLVE BOOLEAN


print ('=========== AULA 3====================================')

arr2 = dsa.array([1,2,3,4,5,6])
print ("Shape do arry",arr2.shape)

print ('===============================================')
