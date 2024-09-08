from sympy import symbols
from sympy.plotting import plot

# Define the symbol
x = symbols('x')

# Define the function
f = 1/x

# Plot the function
plot(f, (x, 0, 10), ylim=(0, 10), title="Graph of f(x) = 1/x", ylabel="f(x)", xlabel="x", line_color='blue')
