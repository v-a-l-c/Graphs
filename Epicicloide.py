#Carrillo Benítez Valentina
#Matemáticas 3

import sympy as sp
from sympy.plotting import plot_parametric

t, a, b = sp.symbols('t a b', real=True)
a_value = 5
b_value = 2

# Ecuaciones paramétricas de la curva original
x = (a + b) * sp.cos(t) - b * sp.cos(((a + b) / b) * t)
y = (a + b) * sp.sin(t) - b * sp.sin(((a + b) / b) * t)

# Ecuaciones paramétricas de la involuta
x_inv = (a + 2*b) / b * ((a + b) * sp.cos(t) + b * sp.cos(((a + b) / b) * t))
y_inv = (a + 2*b) / b * ((a + b) * sp.sin(t) + b * sp.sin(((a + b) / b) * t))

# Graficamos la curva y su involuta
p1 = plot_parametric((x.subs({a: a_value, b: b_value}), y.subs({a: a_value, b: b_value}), (t, 0, 2*sp.pi)), show=False, line_color='blue', title='Curva e Involuta')
p2 = plot_parametric((x_inv.subs({a: a_value, b: b_value}), y_inv.subs({a: a_value, b: b_value}), (t, 0, 2*sp.pi)), show=False, line_color='red')

p1.extend(p2)
p1.show()