import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Ler os dados do excel
df = pd.read_excel("Miniprojeto II/AnexoI-Medicoes_Distancias.xls", usecols="A:B")
data = df.values
data= np.matrix(data.tolist()[8:])

#Filtragem Exponencial
def Filtragem_Exponencial(data, alpha):
    filtered_data = np.zeros(np.shape(data))
    filtered_data[0] = data[0]
    for i in range(1, len(data)):
        filtered_data[i,0] = data[i,0]
        filtered_data[i,1] = alpha * data[i,1] + (1 - alpha) * filtered_data[i-1,1]
    return filtered_data

#Aplicar a vários alphas
for alpha in np.linspace(0,1,9): 
    filtered_data = Filtragem_Exponencial(data, alpha)
    plt.plot(filtered_data[:,0],filtered_data[:,1], label = alpha)

# # Plotting
plt.plot(data[:,0],data[:,1], label = "Dados originais")
plt.legend()
plt.title("Dados Filtrados")
plt.xlabel("Tempo")
plt.ylabel("Distância")
plt.show()

