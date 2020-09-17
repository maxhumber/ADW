# https://www.reddit.com/r/dataisbeautiful/comments/iqplrb/ratings_of_disney_animated_classics_vs_live/g4tgc4z/

import pandas as pd
from matplotlib import pyplot as plt
import gif

df = pd.DataFrame([
    ["The Jungle Book", 7.6, 7.4],
    ["Cinderella", 7.3, 6.9],
    ["Beauty and The Beast", 8, 7.1],
    ["Dumbo", 7.2, 6.3],
    ["Aladdin", 8, 7],
    ["Alice In Wonderland", 7.4, 6.4],
    ["Lady & The Tramp", 7.3, 6.3],
    ["101 Dalmatians", 7.2, 5.7],
    ["The Lion King", 8.5, 6.9],
    ["Mulan", 7.6, 5.5]
], columns=["movie", "original", "live_action"])

df['split'] = df['original'] - df['live_action']
df = df.sort_values('split', ascending=False)
df = df.sort_values('original', ascending=True)

plt.figure(figsize=(5, 10))
plt.scatter(df["original"], df["movie"], s=100)
plt.scatter(df["live_action"], df["movie"], s=100)
plt.xlim([0, 10])


plt.arrow(x=df["original"].values, y=df.index.values, dx=df["live_action"].values, dy=df.index.values)
plt.streamplot(df["original"].values, df.index.values, df["live_action"].values, df.index.values)
