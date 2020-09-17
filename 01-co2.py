# https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions
# https://www.reddit.com/r/dataisbeautiful/comments/ickvfq/oc_two_thousand_years_of_global_temperatures_in/g234slz/

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import gif

df = pd.read_csv("data/co2-concentration-long-term.csv")
df.columns = ['year', 'co2']

# 1
plt.plot(df['year'], df['co2']);

# 2
plt.plot(df['year'], df['co2'])
plt.ylim([0, 500])

# 3
from matplotlib.collections import LineCollection

x = df['year']
y = c = df['co2']
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
plt.figure(figsize=(8, 5))
lc = LineCollection(segments, cmap=plt.get_cmap('viridis'))
lc.set_array(c)
lc.set_linewidth(3)
ax = plt.gca()
ax.add_collection(lc)
plt.xlim(min(x), max(x) + 100_000/10*2);
plt.ylim(0, 500);

# 4

def plot(year):
    d = df[df['year'] <= year]
    x = d['year']
    y = c = d['co2']
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    plt.figure(figsize=(8, 5))
    lc = LineCollection(segments, cmap=plt.get_cmap('viridis'), norm=plt.Normalize(100, 400))
    lc.set_array(c)
    lc.set_linewidth(3)
    ax = plt.gca()
    ax.add_collection(lc)
    plt.xlim(min(x), max(x) + 100_000/10*2);
    plt.ylim(0, 500);

plot(2020)
plt.title("CO2 (ppm) from 800,000BC to Present")
plt.xlabel("Year")
plt.ylabel("CO2 (ppm)")

# 5

@gif.frame
def plot(year):
    d = df[df['year'] <= year]
    x = d['year']
    y = c = d['co2']
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    plt.figure(figsize=(8, 5))
    lc = LineCollection(segments, cmap=plt.get_cmap('viridis'), norm=plt.Normalize(100, 400))
    lc.set_array(c)
    lc.set_linewidth(3)
    ax = plt.gca()
    ax.add_collection(lc)
    plt.xlim(min(x), max(x) + 100_000/10*2);
    plt.ylim(0, 500)
    plt.title("CO2 (ppm) from 800,000BC to Present")
    plt.xlabel("Year")
    plt.ylabel("CO2 (ppm)");

frames = []
for year in range(-800_000, 5_000, 1_000):
    frame = plot(year)
    frames.append(frame)

gif.save(frames, "output/co2.gif", duration=10)


# repeat last image 100 times

gif.options.matplotlib['dpi'] = 150

frames.extend([frames[-1]] * 100)

gif.save(frames, "output/co2.gif", duration=10)
