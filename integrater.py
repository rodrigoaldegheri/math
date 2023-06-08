import sympy as smp

x = smp.symbols("x")
y = smp.cos(x)

print(smp.integrate(y))