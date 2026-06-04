import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024, 2025,2026])
y1 = np.array([10, 20, 25, 30])
y2 = np.array([17,23,38,5])
y3 = np.array([13,15,20,30])

plt.title("Class size", fontsize=25,
                             family="Arial",
                             fontweight="bold",
                             color="#2b30bd")

plt.xlabel("Year", fontsize=20,
                         family="Arial",
                         fontweight="bold",
                         color="#302bbd")


plt.ylabel("Students", fontsize=20,
                             family="Arial",
                             fontweight="bold",
                             color ="#302bbd")
plt.tick_params(axis="both",
                colors="#302bbd")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()
