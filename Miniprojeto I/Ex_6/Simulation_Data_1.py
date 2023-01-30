import numpy as np
import matplotlib.pyplot as plt

# Definir matrizes A e B
A = np.array([[0,1,0], [0, 0, 1], [-7/5, -3/10, 0]])
B = np.array([[0], [0], [3/5]])

# Definir condicao inicial 
x0 = np.array([[0], [0], [0]])

# Definir paço h e numero de paços, a sua multiplicacao sera o tempo final 
h = 0.01
n_steps = 1000

# Definir eixos e configuarazao inicial para o plot
Time = np.linspace(0, n_steps*h, n_steps+1)
fig, axs = plt.subplots(1, len(A), figsize=(15,5))


for Initial_Value in {0.5,1,1.5}: 

    u = np.array([[Initial_Value]])

    # Condição Inicial
    x = x0
    X_plot = {} # Definir um dicionario para Guardar Estados x_n

    for index in range(len(A)):
        X_plot.update( {f"x{index}" : [x0[index,0]]} )

    # Método de Euler
    for i in range(n_steps):
        dx = np.dot(A, x) + np.dot(B, u)
        x = x + dx * h
        # Guardar Dados no dicionario
        for index in range(len(X_plot)):
            X_plot[f"x{index}"].append(x[index,0]) 
    #Implementar o plot 
    for index in range(len(A)):   
        axs[index].plot(Time, X_plot[f"x{index}"], label = f"u = {Initial_Value}")

#Definir estatisticas para o plot
for index in range(len(A)): 
    axs[index].set_xlabel('Time')
    axs[index].set_ylabel(f"X{index}")
    axs[index].set_title(f"X{index}")
    axs[index].legend()
    axs[index].grid()

fig.suptitle('Sistema Dinâmico 1')
plt.show()

print("Simulation and Visualization Complete")

# Print the final state of the system
