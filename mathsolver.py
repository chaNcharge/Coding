from sympy.solvers import solve
from sympy import Symbol

x = Symbol('x')
result = solve(16*x+10 - 1386)
print(result)