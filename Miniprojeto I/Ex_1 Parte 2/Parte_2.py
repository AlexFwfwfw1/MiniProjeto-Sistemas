import matplotlib.pyplot as plt
import numpy as np
import math

def polynomial_func(coeff, x):
    return np.poly1d(np.flip(coeff))(x)

def Minimos_Quadrados(x,y):
    k = len(x)
    n = 2

    X = np.zeros((k, n+1))
    for i in range(k):
        for j in range(n+1):
            X[i,j] = x[i]**j
    return (np.linalg.inv(X.T @ X) @ X.T @ y)

def Calcular_Error(x,y,coeff):
    error_abs,error_rel = 0,0
    z_k_medio = np.average(y)
    for i in range(len(x)):
        error_abs = error_abs + (y[i]-polynomial_func(coeff,x[i]))**2
        error_rel = error_rel + (y[i]-z_k_medio)**2
    error_abs_f = math.sqrt(1/(len(x) + 1) * error_abs)
    error_rel_f = math.sqrt( (error_abs_f**2 )/error_rel )
    
    return error_abs_f,error_rel_f

alpha = [-1,0,2,4,7,10,13,16]
c_l = [0, 1.3, 1.5, 5, 6.8,10.5,9,7]
c_m = [2.2, 1.5, 1.1, 0.7, 0.5,-0.8,-1.1,-0.5]

coeff_cl = Minimos_Quadrados(alpha, c_l)
coeff_cm = Minimos_Quadrados(alpha, c_m)

error_cl_abs,error_cl_rel = Calcular_Error(alpha,c_l,coeff_cl)
error_cm_abs,error_cm_rel = Calcular_Error(alpha,c_m,coeff_cm)

x_vals = np.linspace(-2, 18, 100)

plt.plot(alpha, c_l, 'o', label='Original Data C_L')
plt.plot(x_vals, polynomial_func(coeff_cl, x_vals), '-', label='Obtained Function C_L')
plt.plot(alpha, c_m, 'o', label='Original Data C_M')
plt.plot(x_vals, polynomial_func(coeff_cm, x_vals), '-', label='Obtained Function C_M')

plt.xlabel('Alpha')
plt.ylabel('C_L and C_M')
plt.legend()
plt.show()

print("Erro Abs C_l: " , error_cl_abs , ", Erro Rel C_l: " , error_cl_rel)
print("Erro Abs C_m: " , error_cm_abs , ", Erro Rel C_m: " , error_cm_rel)