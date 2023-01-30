from scipy.optimize import fsolve

a = -0.0594
b = 1.3911
c = 0.6937
d = 0.9

f = lambda x: a*x**2+b*x+c - d

print(fsolve(f, [0,100]))