import numpy as np
from scipy.linalg import expm
np.set_printoptions(suppress=True, precision=3)

#intervalo de tempo considerado
DELTA_T = 0.01

#inicializar uma classe abstrata para facilitar uso de outros valores
class Discrite_Time_System:
    def __init__(self, A, B, C):
        self.A = np.matrix(A)
        self.B = np.matrix(B)
        self.C = np.matrix(C)
        self.Calculate_Accessory_Matrix()
        self.Calculate_G_Matrix()
        self.Print_All_Matrix()
    
    def Calculate_G_Matrix(self):
        self.G = (self.F - np.identity(self.F.shape[0]) ) * np.linalg.inv(self.A) * self.B
        
    #adquirir F primeiro dado que é necessario F para o calculo de G
    def Calculate_Accessory_Matrix(self):
        self.F = expm(self.A*DELTA_T)
        self.A_v = np.linalg.eigvals(self.A)
        self.F_v = np.linalg.eigvals(self.F)
    
    def Print_All_Matrix(self):
        print(f"A = {self.A}\n")
        print(f"B = {self.B}\n")
        print(f"C = {self.C}\n")

        print(f"F = {self.F}\n")
        print(f"G = {self.G}\n")

        print(f"A_v = {self.A_v}\n")
        print(f"F_v = {self.F_v}\n")

A = [
    [0, 1, 0 ],
    [0, 0, 1 ],
    [-7/5, -3/10,0 ],
]

B = [[0], [0] , [3/5]]

C = [[1], [0], [0]]

Simulation1 = Discrite_Time_System(A, B, C)