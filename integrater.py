import sympy as smp

x = smp.symbols("x")
y = smp.cos(x)

integral = smp.integrate(y)
print(integral)