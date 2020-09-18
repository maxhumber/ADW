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
plt.ylim([0, 500]);

# 3
from matplotlib.collections import LineCollection

x = df['year']
y = c = df['co2']
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
plt.figure(figsize=(8, 5))
lc = LineCollection(segments, cmap=plt.get_cmap('plasma'))
lc.set_array(c)
lc.set_linewidth(3)
ax = plt.gca()
ax.add_collection(lc)
plt.xlim(min(x), max(x) + 100_000/10*2)
plt.ylim(0, 500)


# 4

def plot(year):
    d = df[df['year'] <= year]
    x = d['year']
    y = c = d['co2']
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    plt.figure(figsize=(8, 5))
    lc = LineCollection(segments, cmap=plt.get_cmap('plasma'), norm=plt.Normalize(100, 400))
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
    segments = np.concatenate([points[:-2],points[1:-1], points[2:]], axis=1)
    plt.figure(figsize=(8, 5))
    lc = LineCollection(segments, cmap=plt.get_cmap('plasma'), norm=plt.Normalize(100, 400))
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
for year in range(-800_000, 2_000+2_000, 2_000):
    frame = plot(year)
    frames.append(frame)

gif.save(frames, "output/co2.gif", duration=10)

# slow down the ending and make it crisp

@gif.frame
def plot(year):
    d = df[df['year'] <= year]
    x = d['year']
    y = c = d['co2']
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    # overlap the points
    segments = np.concatenate([points[:-2],points[1:-1], points[2:]], axis=1)
    plt.figure(figsize=(7, 4))
    lc = LineCollection(segments, cmap=plt.get_cmap('plasma'), norm=plt.Normalize(100, 400), linewidth=1)
    lc.set_array(c)
    lc.set_linewidth(3)
    ax = plt.gca()
    ax.add_collection(lc)
    plt.xlim(min(x), max(x) + 100_000/10*2);
    plt.ylim(0, 500)
    plt.title("CO2 (ppm) from 800,000BC to Present")
    plt.xlabel("Year")
    plt.ylabel("CO2 (ppm)");

gif.options.matplotlib['dpi'] = 200

period_1 = list(range(-800_000, 0+10_000, 10_000))
period_2 = list(range(0, 2000+5, 5))
period_3 = list(range(2000, 2020+1, 1))
period_4 = [2020] * 100
frames = []

for year in period_1 + period_2 + period_3:
    frame = plot(year)
    frames.append(frame)

gif.save(frames, "output/co2.gif", duration=10)
