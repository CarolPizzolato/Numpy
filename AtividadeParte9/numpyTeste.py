'''calcular a media e o desvio'''
import numpy as np

idades = np.array([3,3,5,3,3,3,3,4,3,3])

media = np.mean(idades)
desvio = np.std(idades)
variancia = np.var(idades)
print ("Media: ", media)
print ("Desvio Padrão: {:.2f}".format(desvio))
print ("Variancia: {:.2f}".format(variancia))


    