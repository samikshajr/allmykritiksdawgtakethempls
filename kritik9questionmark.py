#the second graph (e) is lowk not generating on my screen, but I know the code works for sure bc it has before. do with that what u will...
import sympy as sp

# Define the symbols
x, y = sp.symbols('x y')

# Define the function f(x, y)
f = sp.exp(x) * sp.sin(y) + y**3

# Compute the first partial derivatives
df_dx = sp.diff(f, x)  # Partial derivative with respect to x
df_dy = sp.diff(f, y)  # Partial derivative with respect to y

# Display the results
print("∂f/∂x:", df_dx)
print("∂f/∂y:", df_dy)

#b
# Define the function g(x, y)
g = x**2 * y + x * y**2

# Compute the gradient vector (partial derivatives with respect to x and y)
grad_g_x = sp.diff(g, x)  # Partial derivative with respect to x
grad_g_y = sp.diff(g, y)  # Partial derivative with respect to y

# Evaluate the gradient at the point (1, -1)
grad_g_x_at_point = grad_g_x.subs({x: 1, y: -1})
grad_g_y_at_point = grad_g_y.subs({x: 1, y: -1})

# Gradient vector at (1, -1)
gradient_at_point = (grad_g_x_at_point, grad_g_y_at_point)

# Compute the magnitude of the gradient vector
magnitude = sp.sqrt(grad_g_x_at_point**2 + grad_g_y_at_point**2)

# Display the results
print("Gradient vector at (1, -1):", gradient_at_point)
print("Magnitude of the gradient at (1, -1):", magnitude)

#c
import sympy as sp

# Define the symbols
x, y = sp.symbols('x y')

# Define the function h(x, y)
h = sp.ln(x**2 + y**2)

# Compute the second partial derivatives
d2h_dx2 = sp.diff(h, x, x)  # Second partial derivative with respect to x
d2h_dy2 = sp.diff(h, y, y)  # Second partial derivative with respect to y
d2h_dxdy = sp.diff(h, x, y)  # Mixed partial derivative

# Display the results
print("∂²h/∂x²:", d2h_dx2)
print("∂²h/∂y²:", d2h_dy2)
print("∂²h/∂x∂y:", d2h_dxdy)

# Symmetry of mixed partial derivatives
print("\nSymmetry Check:")
print("∂²h/∂x∂y = ∂²h/∂y∂x:", sp.diff(h, x, y) == sp.diff(h, y, x))

#d
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the symbols and function
x, y = sp.symbols('x y')
j = x**3 - 3*x*y + y**3

# Convert the SymPy expression to a numerical function
j_func = sp.lambdify((x, y), j, 'numpy')

# Create a grid of x and y values and evaluate j on this grid
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = j_func(X, Y)

# Plot the contour
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $j(x, y) = x^3 - 3xy + y^3$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
#im geeking over contour plot isnt it quite nice?

#e
import sympy as sp

# Define the symbols
x, y = sp.symbols('x y')

# Define the function h(x, y)
h = x**3 + y**3 - 3*x*y

# Compute the second partial derivatives
d2h_dx2 = sp.diff(h, x, x)  # Second partial derivative with respect to x
d2h_dy2 = sp.diff(h, y, y)  # Second partial derivative with respect to y
d2h_dxdy = sp.diff(h, x, y)  # Mixed partial derivative

# Display the results
print("∂²h/∂x²:", d2h_dx2)
print("∂²h/∂y²:", d2h_dy2)
print("∂²h/∂x∂y:", d2h_dxdy)

# Symmetry Check
print("\nSymmetry Check:")
print("∂²h/∂x∂y = ∂²h/∂y∂x:", sp.diff(h, x, y) == sp.diff(h, y, x))