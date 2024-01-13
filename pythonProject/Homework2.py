import numpy as np
import matplotlib.pyplot as plt

# The sample comprising of 10 data points
S = [1, 0, 2, 3, 6, 1, 2, 8, 1, 3]

# a. Compute the given sample S and let that be S
alpha = np.mean(S)
print("Mean value of the given sample: ", alpha)

# Generate a bootstrap sample S* from the given sample S and compute mean value
bootstrap_sample = np.random.choice(S, size=len(S), replace=True)
alpha_star = np.mean(bootstrap_sample)
print("Mean value of bootstrap sample: ", alpha_star)

# Draw 100 bootstrap samples and compute  the minimum and maximum sample means
sample_means = []
raw_residuals = []
for i in range(100):
    bootstrap_sample_i = np.random.choice(S, size=len(S), replace=True)
    alpha_star_i = np.mean(bootstrap_sample_i)
    sample_means.append(alpha_star_i)
    raw_residuals.append(alpha - alpha_star_i)

# Compute the minimum and maximum sample means
min_sample_mean = min(sample_means)
max_sample_mean = max(sample_means)
print("Minimum Sample Mean: ", min_sample_mean)
print("Maximum Sample Mean: ", max_sample_mean)

# Plot raw residuals against i
plt.plot(range(100), raw_residuals)
plt.xlabel('i')
plt.ylabel('Raw residual')
plt.title('Raw Residual vs. i')
plt.show()

# Draw 1000 bootstrap samples  and compute their mean
bootstrap_sample_means_1000 = []
for i in range(1000):
    bootstrap_sample = np.random.choice(S, size=len(S), replace=True)
    bootstrap_sample_mean = np.mean(bootstrap_sample)
    bootstrap_sample_means_1000.append(bootstrap_sample_mean)

# Average the 1000 bootstrap sample means
average_bootstrap_sample_mean = np.mean(bootstrap_sample_means_1000)
print("Average of 1000 bootstrap sample means: ", average_bootstrap_sample_mean)

# Compute bias
bias = average_bootstrap_sample_mean - alpha
print("Bias of the bootstrapped samples: ", bias)

# Compute variance
variance = np.var(bootstrap_sample_means_1000)
print("Variance of the bootstrapped samples: ", variance)

# Compute unbiased estimate of the sample mean
unbiased_estimate = alpha + bias
print("Unbiased estimate of the sample mean: ", unbiased_estimate)

# Compute MSE of the simulation
mse = variance + bias**2
print("MSE of the simulation: ", mse)
