import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# create a plot
fig, ax = plt.subplots(figsize=(7,4))

# Plot the data
plt.plot(x, y)

# Add grid
ax.grid(True)

# set the title
ax.set_title('Basic Plot with Grids')

# Show the plot
plt.show()