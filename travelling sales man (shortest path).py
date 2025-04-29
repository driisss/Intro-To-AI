import numpy as np
import matplotlib.pyplot as plt
import itertools

# Generate 5 random cities (coordinates)
np.random.seed(42)  # for consistent results
cities = np.random.rand(5, 2) * 100  # 5 cities, 2D coordinates in [0, 100]

# Calculate distance between two points
def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

# Total path length
def path_length(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance(path[i], path[i + 1])
    total += distance(path[-1], path[0])  # Return to starting city
    return total

# Find the shortest path
min_path = None
min_length = float('inf')

for perm in itertools.permutations(cities):
    current_length = path_length(perm)
    if current_length < min_length:
        min_length = current_length
        min_path = perm

min_path = np.array(min_path)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(min_path[:, 0], min_path[:, 1], 'o-', label='Shortest path')
# Close the loop (return to starting city)
plt.plot([min_path[-1, 0], min_path[0, 0]], [min_path[-1, 1], min_path[0, 1]], 'o-')
for idx, (x, y) in enumerate(min_path):
    plt.text(x, y, f'City {idx}', fontsize=12)
plt.title(f'Shortest path length: {min_length:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
