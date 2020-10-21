import pandas
import numpy as np
from matplotlib import pyplot as plt

# scatters

n = 1000
a = np.random.uniform(0, 100, size=n)
b = np.random.normal(0, 20, size=n)

plt.scatter(a, b);

# lines

plt.plot(range(10), range(10), c="r");

# bars

plt.bar(["A", "B", "C"], [10, 20, 15], color='#660066');

# ticks

plt.figure(figsize=(5, 5))
plt.scatter(a, b, alpha=1/10)
plt.xticks([])
plt.yticks([]);

# limits

plt.figure(figsize=(5, 5))
plt.scatter(a, b, alpha=1/5, color='orange')
plt.ylim([-100, 100])
plt.xlim([0, 100]);
