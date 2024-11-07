import numpy as np
import matplotlib.pyplot as plt

# Define the Triangular Membership Function
def triangular(x, a, b, c):
    # a, b, c are the left, center, and right values of the triangle
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

# Define the Trapezoidal Membership Function
def trapezoidal(x, a, b, c, d):
    # a, b, c, d are the left, start, end, and right values of the trapezoid
    return np.maximum(np.minimum((x - a) / (b - a), 1, (d - x) / (d - c)), 0)

# Define the Gaussian Membership Function
def gaussian(x, mean, sigma):
    # mean is the center of the Gaussian, and sigma is the standard deviation
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

# Create a range of x values for plotting
x = np.linspace(0, 10, 1000)

# Plot Triangular Membership Function
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
y_triangular = triangular(x, 2, 5, 8)  # a=2, b=5, c=8 for the triangle
plt.plot(x, y_triangular, label="Triangular Membership", color="b")
plt.title("Triangular Membership Function")
plt.xlabel("x")
plt.ylabel("Membership value")
plt.grid(True)

# Plot Trapezoidal Membership Function
plt.subplot(3, 1, 2)
y_trapezoidal = trapezoidal(x, 2, 3, 7, 8)  # a=2, b=3, c=7, d=8 for the trapezoid
plt.plot(x, y_trapezoidal, label="Trapezoidal Membership", color="g")
plt.title("Trapezoidal Membership Function")
plt.xlabel("x")
plt.ylabel("Membership value")
plt.grid(True)

# Plot Gaussian Membership Function
plt.subplot(3, 1, 3)
y_gaussian = gaussian(x, 5, 1)  # mean=5, sigma=1 for the Gaussian curve
plt.plot(x, y_gaussian, label="Gaussian Membership", color="r")
plt.title("Gaussian Membership Function")
plt.xlabel("x")
plt.ylabel("Membership value")
plt.grid(True)

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
