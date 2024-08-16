#Carrillo Benítez Valentina
#Matemáticas 3

import sympy as sp
from sympy.plotting import plot_parametric

t, a = sp.symbols('t a', real=True)
a_value = 1

# Ecuaciones paramétricas de la curva original
x = t**2
y = a * t**3

# Ecuaciones paramétricas de la involuta
x_inv = (t**2) / 3 - 8 / (27 * a**2)
y_inv = -4 * t / (9 * a)

# Graficamos la curva y su involuta
p1 = plot_parametric((x, y.subs(a, a_value), (t, -2, 2)), show=False, line_color='blue', title='Curva e Involuta')
p2 = plot_parametric((x_inv.subs(a, a_value), y_inv.subs(a, a_value), (t, -2, 2)), show=False, line_color='red')

p1.extend(p2)
p1.show()