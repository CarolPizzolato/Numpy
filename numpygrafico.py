import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
filename = r"D:\Vs code\#DSAarquivos\Parte 9\Notebooks\dataset.csv"
df = pd.read_csv(filename)

# Definir cores para cada espécie
colors = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}

# Criar o gráfico de dispersão com cores por espécie
plt.figure(figsize=(8,6))
for species, color in colors.items():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'], c=color, label=species)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Gráfico de Dispersão: Sepal Length vs Sepal Width")
plt.legend()
plt.show()
