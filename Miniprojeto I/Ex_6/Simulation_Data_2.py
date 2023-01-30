import numpy as np
import matplotlib.pyplot as plt

# Define the matrices A and B
A = np.array([[0, 1, 0, 0],
              [0, 0, 1 , 0],
              [0, 0,0,1],
              [-3, -1,-5,-2]])
B = np.array([[0],
              [0],
              [0],
              [7.2]])

# Define the initial condition x0 and the input u
x0 = np.array([[0], [0], [0], [0]])

# Define the time step and the number of steps to simulate
h = 0.01
n_steps = 1000

Time = np.linspace(0, n_steps*h, n_steps+1)
fig, axs = plt.subplots(1, len(A), figsize=(15, 5))

for Initial_Value in {0.5, 1, 1.5}:

    u = np.array([[Initial_Value]])

    # Set the initial condition
    x = x0
    X_plot = {}

    for index in range(len(A)):
        X_plot.update({f"x{index}": [x0[index, 0]]})

    # Use Euler's method to simulate the system
    for i in range(n_steps):
        dx = np.dot(A, x) + np.dot(B, u)
        x = x + dx * h
        for index in range(len(X_plot)):
            X_plot[f"x{index}"].append(x[index, 0])

    for index in range(len(A)):
        # print(f"X{index}, inital = {Initial_Value}" )
        # print(X_plot[f"x{index}"])
        axs[index].plot(Time, X_plot[f"x{index}"],
                        label=f"u = {Initial_Value}")

for index in range(len(A)):
    axs[index].set_xlabel('Time')
    axs[index].set_ylabel(f"X{index}")
    axs[index].set_title(f"X{index}")
    axs[index].legend()
    axs[index].grid()

fig.suptitle('Sistema Dinâmico 2')
plt.show()

print("Simulation and Visualization Complete")

# Print the final state of the system
