import matplotlib.pyplot as plt

# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data on the axis
ax.plot(x, y)

# Set the title and axis labels
ax.set_title('My First Matplotlib Plot')
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')

# Show the plot
plt.show()
