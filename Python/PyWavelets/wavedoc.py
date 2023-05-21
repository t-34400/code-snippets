import pywt
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 1, 1000)
data = np.random.normal(0, 1, len(t)) * np.sin(50 * 2 * np.pi * t) * np.exp(-10 * t)

wavelet = 'db4'
level = 6

coeffs = pywt.wavedec(data, wavelet, level=level)


plt.figure(figsize=(10, 6))
plt.subplot(level + 2, 1, 1)
reconstructed_data = pywt.waverec(coeffs, wavelet)
plt.plot(data)
plt.plot(reconstructed_data)

for i, c in enumerate(coeffs):
    plt.subplot(level + 2, 1, i + 2)
    plt.plot(c)
    plt.ylabel(f"Level {i+1}")
plt.xlabel("Sample")
plt.tight_layout()
plt.show()
