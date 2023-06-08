import numpy as np
import sympy as smp

x = smp.symbols("x")
y = x**2

derivative = smp.diff(y)
print(derivative)