import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2

# Define the range for x values
x_values = np.linspace(-5, 5, 100)
x_values = x_values[x_values != 0]  # Remove x = 0 to avoid division by zero

# Calculate y values for the function
y_values = f(x_values)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = 1/x', color='blue')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Define two points (x1, y1) and (x2, y2)
x1, x2 = 0, 0.1
y1, y2 = f(x1), f(x2)

# Plot the points on the graph
plt.plot([x1, x2], [y1, y2], 'ro')  # Red points
plt.text(x1, y1, f'({x1:.2f}, {y1:.2f})', fontsize=10, ha='right')
plt.text(x2, y2, f'({x2:.2f}, {y2:.2f})', fontsize=10, ha='left')

# Draw a line between the points
plt.plot([x1, x2], [y1, y2], 'r--', label='Line between points')

# Calculate the slope
slope = (y2 - y1) / (x2 - x1)
plt.title(f'Graph of f(x) = 1/x\nSlope between points ({x1}, {y1}) and ({x2}, {y2}): {slope:.2f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-10, 10)
plt.legend()
plt.grid(True)
plt.show()

# Print the slope
print(f"The slope between the points ({x1}, {y1}) and ({x2}, {y2}) is: {slope:.2f}")
