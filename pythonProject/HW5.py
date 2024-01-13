import numpy as np

# Generate a 100x100 matrix with random entries
matrix = np.random.rand(100, 100)

# Compute the eigenvalues
eigenvalues = np.linalg.eigvals(matrix)

# Plot the eigenvalues
import matplotlib.pyplot as plt
plt.scatter(np.arange(len(eigenvalues)), eigenvalues, s=1)
plt.xlabel('Index')
plt.ylabel('Eigenvalue')
plt.title('Eigenvalues of Random Matrix')
plt.show()
