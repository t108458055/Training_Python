import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the sine waves
frequency1 = 5  # Frequency of the first sine wave
frequency2 = 8  # Frequency of the second sine wave
amplitude1 = 1  # Amplitude of the first sine wave
amplitude2 = 1  # Amplitude of the second sine wave
phase1 = 0  # Phase of the first sine wave
phase2 = 0  # Phase of the second sine wave
sampling_rate = 100  # How many points to sample per unit interval
t = np.arange(0, 1, 1/sampling_rate)  # Time vector

# Generate the sine waves
y1 = amplitude1 * np.sin(2 * np.pi * frequency1 * t + phase1)
y2 = amplitude2 * np.sin(2 * np.pi * frequency2 * t + phase2)

# Sum the two sine waves
y_sum = y1 + y2

# Plotting
plt.figure(figsize=(10, 7))
plt.subplot(311)
plt.plot(t, y1)
plt.title('First Sine Wave')
plt.subplot(312)
plt.plot(t, y2)
plt.title('Second Sine Wave')
plt.subplot(313)
plt.plot(t, y_sum)
plt.title('Sum of the Two Sine Waves')
plt.xlabel('Time')
plt.tight_layout()
plt.show()
