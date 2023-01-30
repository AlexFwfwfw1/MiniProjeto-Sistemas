import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation
def dydt(y, t):
    return [y[1] + 0.5*y[0], y[0] + y[1]]

# Define the time range
t = np.linspace(0, 10, 100)

# Define the range for the x and y variables
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)

# Create a meshgrid of the x and y variables
X, Y = np.meshgrid(x, y)

# Calculate the derivatives using the differential equation
DX, DY = dydt([X, Y], t)

# Plot the vector field
mappable = plt.pcolor(X, Y, np.hypot(DX, DY), cmap='YlOrRd')
plt.quiver(X, Y, DX, DY)
plt.xlabel('Y')
plt.ylabel('Y_DOT')
plt.colorbar(mappable) # Add colorbar
plt.show()
