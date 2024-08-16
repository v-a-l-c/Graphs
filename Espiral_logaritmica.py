#Carrillo Benítez Valentina
#Matemáticas 3

import sympy as sp
from sympy.plotting import plot_parametric, plot3d_parametric_line

t, b = sp.symbols('t b', real=True)
b_value = 0.1

# Ecuaciones paramétricas de la espiral logarítmica
x = sp.exp(b*t) * sp.cos(t)
y = sp.exp(b*t) * sp.sin(t)

# Ecuaciones paramétricas de la involuta
x_inv = sp.exp(b*t) * sp.sin(t) / b
y_inv = sp.exp(b*t) * sp.cos(t) / b

# Graficamos la espiral logarítmica y su involuta
p1 = plot_parametric((x.subs(b, b_value), y.subs(b, b_value), (t, 0, 10*sp.pi)), show=False, line_color='blue', title='Espiral Logarítmica e Involuta')
p2 = plot_parametric((x_inv.subs(b, b_value), y_inv.subs(b, b_value), (t, 0, 10*sp.pi)), show=False, line_color='red')

p1.extend(p2)
p1.show()