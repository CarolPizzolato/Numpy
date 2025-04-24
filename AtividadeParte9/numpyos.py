import numpy as np
import os
    
filename = r"D:\Vs code\#DSAarquivos\Parte 9\Notebooks\dataset.csv"

print ("Origem do arquivo: ",filename)

'''
if os.path.exists(filename):
    print("Arquivo encontrado:", filename)
    arr13 = np.loadtxt(filename, delimiter=',',usecols= (0,1,2,3), skiprows = 1)
    print (arr13)
else:
    print("Arquivo NÃO encontrado!")

'''
#filename = r"D:\Vs code\#DSAarquivos\Parte 9\Notebooks\dataset.csv"
var1, var2 = np.loadtxt(filename, delimiter = ',', usecols = (0,1), skiprows = 1, unpack = True)
#AGORA VAMOS USAR AJUDA DE UM PACOTE

import matplotlib.pyplot as plt
plt.plot(var1, var2, 'o', markersize=8, color='red')
plt.show()


