#Carrillo Benítez Valentina
#Matemáticas 3

import sympy as sp
from sympy.plotting import plot_parametric

t, a = sp.symbols('t a', real=True)
a_value = 1

# Ecuaciones paramétricas de la curva original
x = a * (t - sp.sin(t))
y = a * (1 - sp.cos(t))

# Ecuaciones paramétricas de la involuta
x_inv = a * (t + sp.sin(t))
y_inv = a * (3 + sp.cos(t))

# Graficamos la curva y su involuta
p1 = plot_parametric((x.subs(a, a_value), y.subs(a, a_value), (t, -10, 10)), show=False, line_color='blue', title='Curva e Involuta')
p2 = plot_parametric((x_inv.subs(a, a_value), y_inv.subs(a, a_value), (t, -10, 10)), show=False, line_color='red')

p1.extend(p2)
p1.show()