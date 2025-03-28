import numpy as np
import matplotlib.pyplot as plt

def generate_sin_with_noise(n_points=10000, period=168, noise_level=0.1, burst_prob=0.01, burst_amplitude=0.5):
    x = np.linspace(0, n_points, n_points)
    y = np.sin(2 * np.pi * x / period)
    
    noise = np.random.normal(0, noise_level, n_points)
    noisy_sin = y + noise
    
    burst_mask = np.random.random(n_points) < burst_prob
    burst_noise = np.random.normal(0, burst_amplitude, n_points)
    burst_noise[~burst_mask] = 0
    final_sin = noisy_sin + burst_noise
    
    return final_sin

n_curves = 4
n_points = 10000
period = 168

curves = {}
for i in range(n_curves):
    np.random.seed(i) 
    curves[f'arr_{i}'] = generate_sin_with_noise(
        n_points=n_points,
        period=period,
        noise_level=0.1, 
        burst_prob=0.01,  
        burst_amplitude=0.5  
    )


np.savez('data/sin_data.npz', **curves)
