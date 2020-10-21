# https://www.reddit.com/r/dataisbeautiful/comments/ipx2qz/all_tom_cruises_wives_were_33_at_time_of_divorceoc/

import pandas as pd
from matplotlib import pyplot as plt
import gif

df = pd.read_csv("data/leo.csv")

# attempt 1

plt.figure(figsize=(7, 4), dpi=150)
plt.plot(df['year'], df['age'], color="orange", linewidth=2)
plt.scatter(df['year'], df['age'], color='orange')
plt.bar(x=df['year'], height=df['partner_age'].fillna(0))

# attempt 2

plt.figure(figsize=(7, 4), dpi=150)
plt.plot(df['year'], df['age'], color="black", linewidth=2, marker='o')
for partner in df.partner.unique():
    subdf = df[df['partner'] == partner]
    plt.bar(x=subdf['year'], height=subdf['partner_age'].fillna(0), label=partner)
plt.hlines(y=25, xmin=df['year'].min(), xmax=df['year'].max(), color="red")
plt.title("Leo can't date above 25")
plt.xlabel("Year")
plt.ylabel("Leo's Age")
plt.legend(loc="upper right");

# try to prove out one frame

d = df[df["year"] <= 2010]

plt.figure(figsize=(7, 4), dpi=150)
plt.plot(d['year'], d['age'], color="black", linewidth=2, marker='o')
for partner in d.partner.unique():
    subdf = d[d['partner'] == partner]
    plt.bar(x=subdf['year'], height=subdf['partner_age'].fillna(0), label=partner)
plt.hlines(y=25, xmin=df['year'].min() - 1, xmax=df['year'].max() + 1, color="red")
plt.title("Leo won't date above 25")
plt.xlabel("Year")
plt.ylabel("Age")
plt.xticks(range(1998, 2020+1, 3))
plt.xlim([1998, 2020])
plt.ylim([16, 46])


# make it into a function

@gif.frame
def plot(year):
    d = df[df["year"] <= year]
    plt.figure(figsize=(7, 4))
    plt.plot(d['year'], d['age'], color="black", linewidth=2, marker='o')
    for partner in d.partner.unique():
        subdf = d[d['partner'] == partner]
        plt.bar(x=subdf['year'], height=subdf['partner_age'].fillna(0), label=partner)
    plt.hlines(y=25, xmin=df['year'].min() - 1, xmax=df['year'].max() + 1, color="red")
    plt.title("Leo won't date above 25")
    plt.xlabel("Year")
    plt.ylabel("Age")
    plt.xticks(range(1998, 2020+1, 3))
    plt.xlim([1998, 2020])
    plt.ylim([16, 46])

frames = []
for year in range(1999, 2020):
    frame = plot(year)
    frames.append(frame)

gif.options.matplotlib["dpi"] = 300
gif.save(frames, "output/leo.gif", duration=5, unit='seconds', between="startend")
