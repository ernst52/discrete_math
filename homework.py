import matplotlib.pyplot as plt
import numpy as np

# parameters
n = 6
a = 7
i_values = np.arange(0, n+1)

# functions
f1 = i_values + n                  # i + n
f2 = a * i_values                  # a * i
f3 = a ** i_values                 # a^i
f4 = np.cumsum(i_values)           # Σ i
f5 = np.cumprod(i_values+1)        # Π i 

# plot
plt.plot(i_values, f1, label="i+n")
plt.plot(i_values, f2, label="a×i")
plt.plot(i_values, f3, label="a^i")
plt.plot(i_values, f4, label="Σ a_i")
plt.plot(i_values, f5, label="Π a_i")

plt.xlabel("i")
plt.ylabel("Value")
plt.title(f"Line Plot of Equations (n={n}, a={a})")
plt.legend()
plt.grid(True)
plt.show()
