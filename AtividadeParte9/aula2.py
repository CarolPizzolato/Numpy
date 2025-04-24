import numpy as dsa # posso dar o nome que quero

#                 0 1 2 3 4 5 6 7 8 9  10 11 12 13 
arr1 = dsa.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

#imprimindo ate

print (arr1[:4]) # o segundo valor nao faz parte do resultado

#o array numpy aceita somar indicies ex: (arr1[:4+1])
#outra coisa que posso fazer

indices = [1,3,5,6,7]
print (arr1 [indices])

divide2 = (arr1 %2 == 0) # cada elemento do array é divido ´pr 2

#================================================================#

#AULA 3

arr2 = dsa.array([1,2,3,4,5,6])

print (arr2.shape)
