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

# text

plt.text(x=0.5, y=0.5, s="This is text",
    color="#005555", fontsize=16, va="center", ha="center"
);

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

# backgrounds

hexcode = "#009933"
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_facecolor(hexcode)

# grid spec

grid = plt.GridSpec(
    nrows=2,
    ncols=2,
    wspace=0.2,
    hspace=0.2,
)

# [(0, 0), (0, 1)]
# [(1, 0), (1, 1)]

# grid[row, columns]

p1 = plt.subplot(grid[0, :2])
p2 = plt.subplot(grid[1, 0])
p3 = plt.subplot(grid[1, 1])

p3.set_facecolor(hexcode);

# images

from PIL import Image
from matplotlib import pyplot as plt

file = 'data/wave.jpg'

im = Image.open(file)
plt.imshow(im);
