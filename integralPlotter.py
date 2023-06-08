import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

x = smp.symbols("x")
y = smp.cos(x)

raw = smp.integrate(y)
elaborated = smp.lambdify(x, raw, np)

print(raw)

x = np.arange(-10,10,0.1)
y = elaborated(x)

plt.title("Integral of cos(x)")
plt.plot(x,y)
plt.show()