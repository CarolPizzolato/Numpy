import numpy as np

idade = np.array([ 15,24,45,89,95,12,42])

print (np.mean(idade))
print ("Desvio padrão de idades: {:.2f}". format(np.std(idade)))
print ("A variancia é: {:.2f}".format(np.var(idade)))
