#Carrillo Benítez Valentina
#Matemáticas 3

import sympy as sp
from sympy.plotting import plot_parametric

t = sp.symbols('t', real=True)

# Ecuaciones paramétricas de la curva original
x = 1/2 * (3 * sp.cos(t) - sp.cos(3*t))
y = 1/2 * (3 * sp.sin(t) - sp.sin(3*t))

# Ecuaciones paramétricas de la involuta
x_inv = 4 * sp.cos(t)**3
y_inv = 3 * sp.sin(t) + sp.sin(3*t)

# Graficamos la curva y su involuta
p1 = plot_parametric((x, y, (t, 0, 2*sp.pi)), show=False, line_color='blue', title='Curva e Involuta')
p2 = plot_parametric((x_inv, y_inv, (t, 0, 2*sp.pi)), show=False, line_color='red')

p1.extend(p2)
p1.show()