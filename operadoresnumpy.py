import numpy as np

'''
array1= np.arange(1,10)
print (np.sum (array1))
print (np.prod (array1))
'''
'''
vet1 = np.array([1,2,3])
vet2 = np.array([3,4,5])
soma = np.add(vet1,vet2)
print (soma)
'''
#multiplicação de matrizes:
'''
matriz1 = np.array([[1,3,2],[4,4,5]]) 
matriz2 = np.array([[7,8],[1,2],[9,10]])

print (matriz1.shape)
print (matriz2.shape)
print (np.dot(matriz1,matriz2))
#podemos também multiplicar assim @

# outra forma de fazer:
produto = matriz1 @ matriz2
print (produto)


'''

#fatiamento
#Função diag cria uma matriz de dimensão  2 e  diagonal 3 elemtnos, 0, 1 e 2

vetorfatiado = np.diag(np.arange(3))