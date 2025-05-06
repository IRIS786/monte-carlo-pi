import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(num_samples):
    points = np.random.rand(num_samples, 2)
    inside = np.sum(np.linalg.norm(points, axis=1) <= 1.0)
    pi_estimate = 4 * inside / num_samples
    return pi_estimate, points

if __name__ == "__main__":
    num_samples = 100_000
    pi_estimate, points = estimate_pi(num_samples)
    
    # Plotting
    plt.figure(figsize=(6, 6))
    inside = points[np.linalg.norm(points, axis=1) <= 1.0]
    outside = points[np.linalg.norm(points, axis=1) > 1.0]
    plt.scatter(inside[:,0], inside[:,1], color='blue', s=1)
    plt.scatter(outside[:,0], outside[:,1], color='red', s=1)
    plt.title(f"Estimation of π: {pi_estimate:.5f}")
    plt.savefig('pi_estimation.png')
    plt.close()