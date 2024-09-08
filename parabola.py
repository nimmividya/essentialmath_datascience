from sympy import symbols
from sympy.plotting import plot

# Define the symbol
x = symbols('x')

# Define the function
f = x**2

# Plot the function
plot(f, (x, -5, 5), ylim=(0, 2), title="Graph of f(x) = 1/x", ylabel="f(x)", xlabel="x", line_color='blue')
