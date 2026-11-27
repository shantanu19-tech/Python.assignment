import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Create multiple plots
plt.figure(figsize=(10, 8))

# 1. Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 2. Scatter Plot
plt.subplot(2, 2, 2)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 3. Bar Chart
plt.subplot(2, 2, 3)
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 4. Box Plot
plt.subplot(2, 2, 4)
plt.boxplot(y)
plt.title("Box Plot")
plt.ylabel("Values")

# Display all plots
plt.tight_layout()
plt.show()