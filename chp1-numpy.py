import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the range of x values
x = np.linspace(-1, 10, 400)  # Creates 400 points between -10 and 10

# Step 2: Compute the corresponding y values for the function f(x) = 2x + 1
y = 2 * x + 1

# Step 3: Plot the graph
plt.plot(x, y, label="f(x) = 2x + 1", color='b')  # 'b' is the color blue

# Step 4: Customize the graph
plt.axhline(0, color='purple', linewidth=0.5)  # x-axis
plt.axvline(0, color='green', linewidth=0.5)  # y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Add grid lines
plt.title("Graph of f(x) = 2x + 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Step 5: Display the plot
plt.show()
