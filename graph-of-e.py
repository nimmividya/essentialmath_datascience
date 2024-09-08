from sympy import symbols
from sympy.plotting import plot

# Define the symbol
x = symbols('x')

# Define the function
f = (1/x)**x

# Plot the function
plot(f, (x, 0, 100), ylim=(0, 2), title="Graph of f(x) = 1/x", ylabel="f(x)", xlabel="x", line_color='blue')
