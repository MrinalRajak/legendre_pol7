
#legendre polynomial
#(8) (x**2-1)*P'(n,x) = (n+1)*(P(n+1,x)-x*P(n,x))

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=int(input("Enter the n: "))

def f(x):
    return legendre(n)(x)
LHS=(x**2-1)*derivative(f,x,order=15)
RHS=(n+1)*(legendre(n+1)(x))-(n+1)*x*f(x)
print("LHS: ",LHS)
print("RHS: ",RHS)
