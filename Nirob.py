import  matplotlib.pyplot as plt
import numpy as np


x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17,23, 38, 5])
y3 = np.array([13, 15, 20, 30])


line_style = dict(marker = ".",
                markersize = 30,
                markerfacecolor= "#429ef5",
                markeredgecolor = "#429ef5",
                linestyle = "solid",
                linewidth=4)

plt.plot(x, y1, color = "#4284f5", **line_style)
plt.plot(x, y2, color="#a84e32", **line_style)
plt.plot(x, y3, color ="#a89532", **line_style)

plt.show()

