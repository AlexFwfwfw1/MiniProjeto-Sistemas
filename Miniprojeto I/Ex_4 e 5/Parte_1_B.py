import numpy as np
from scipy.linalg import expm, sinm, cosm
from Matrix_Latex import lprint


np.set_printoptions(suppress=True, precision=3)


DELTA_T = 0.01

class Least_Squares_Simulation:
    def __init__(self, A, B, C):
        self.A = np.matrix(A)
        self.B = np.matrix(B)
        self.C = np.matrix(C)

    def Estimate_Epsilon(self):
        self.Epslone, self.N = 1, 0
        while self.Epslone > 10E-4:
            self.N = self.N + 1
            self.Epslone = np.linalg.norm((self.A**(self.N-1))/(np.math.factorial(self.N)), ord='fro')
    
    def Estimate_Drag_Coeficient(self):
        self.C_d = 0
        for k in range(1,self.N):
            self.C_d = ((self.A**(k-1))*((DELTA_T)**k))/(np.math.factorial(k))+self.C_d
        
        return self.C_d
    def Calculate_Accessory_Matrix(self):
        self.A_b = expm(self.A*DELTA_T)
        self.B_d = self.C_d*self.B
        self.A_v = np.linalg.eigvals(self.A)
        self.A_b_v = np.linalg.eigvals(self.A_b)
    
    def Print_All_Matrix(self):
        print(f"A = {self.A}\n")
        print(f"A_b = {self.A_b}\n")
        print(f"A_v = {self.A_v}\n")
        print(f"A_b_v = {self.A_b_v}\n")
        print(f"B = {self.B}\n")
        print(f"B_d = {self.B_d}\n")
        print(f"C = {self.C}\n")
        print(f"C_d = {self.C_d}\n")
        print(f"N = {self.N}\n")
        print(f"Epslone = {self.Epslone}\n")
        # print(lprint.lprintm(self.B_d))

    # def Simulate(self, initial):



A = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [-3, -1, -5, -2]
]

B = [[0], [0], [0], [7.2]]

C = [[1], [0], [0], [0]]


Simulation1 = Least_Squares_Simulation(A, B, C)

Simulation1.Estimate_Epsilon()
Simulation1.Estimate_Drag_Coeficient()
Simulation1.Calculate_Accessory_Matrix()
Simulation1.Print_All_Matrix()
