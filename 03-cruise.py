# https://www.reddit.com/r/dataisbeautiful/comments/ipx2qz/all_tom_cruises_wives_were_33_at_time_of_divorceoc/

import pandas as pd
from matplotlib import pyplot as plt
import gif

df = pd.DataFrame({
    'year': range(1985, 2015),
    'age': range(23, 53)
})

df['partner'] = None
df.loc[(df.year >= 1987) & (df.year <= 1990), ['partner']] = 'Mimi Rogers'
df.loc[(df.year >= 1991) & (df.year <= 2001), ['partner']] = 'Nicole Kidman'
df.loc[(df.year >= 2006) & (df.year <= 2012), ['partner']] = 'Katie Holmes'
df['partner_age'] = None
df['partner_age'][2:6]= range(30, 33+1)
df['partner_age'][6:17]= range(23, 33+1)
df['partner_age'][21:28] = range(27, 33+1)

# attempt 1

plt.figure(figsize=(7, 4), dpi=150)
plt.plot(df['year'], df['age'], color="orange", linewidth=2)
plt.scatter(df['year'], df['age'], color='orange')
plt.bar(x=df['year'], height=df['partner_age'].fillna(0))

# attempt 2

rogers = df[df['partner'] == "Mimi Rogers"]
kidman = df[df['partner'] == "Nicole Kidman"]
holmes = df[df['partner'] == "Katie Holmes"]

plt.figure(figsize=(7, 4), dpi=150)
plt.plot(df['year'], df['age'], color="orange", linewidth=2, marker='o')
plt.bar(x=rogers['year'], height=rogers['partner_age'].fillna(0), label="Mimi Rogers")
plt.bar(x=kidman['year'], height=kidman['partner_age'].fillna(0), label="Nicole Kidman")
plt.bar(x=holmes['year'], height=holmes['partner_age'].fillna(0), label="Katie Holmes")
plt.hlines(y=33, xmin=df['year'].min(), xmax=df['year'].max(), color="red")
plt.title("Tom Cruise Hates 34 year-olds")
plt.xlabel("Year")
plt.ylabel("Tom's Age")
plt.legend(loc="upper right");


# try to prove out one frame

year = 1991
d = df[df['year'] <= year]

rogers = d[d['partner'] == "Mimi Rogers"]
kidman = d[d['partner'] == "Nicole Kidman"]
holmes = d[d['partner'] == "Katie Holmes"]

plt.figure(figsize=(7, 4), dpi=150)
plt.plot(d['year'], d['age'], color="orange", linewidth=2, marker='o')
plt.bar(x=rogers['year'], height=rogers['partner_age'].fillna(0), label="Mimi Rogers")
plt.bar(x=kidman['year'], height=kidman['partner_age'].fillna(0), label="Nicole Kidman")
plt.bar(x=holmes['year'], height=holmes['partner_age'].fillna(0), label="Katie Holmes")
plt.hlines(y=33, xmin=d['year'].min(), xmax=d['year'].max(), color="red")
plt.title("Women Expire at 33 According to Tom Cruise")
plt.xlabel("Year")
plt.ylabel("Age")
plt.xlim([1985, 2015])
plt.ylim([20, 55])


# make it into a function

@gif.frame
def plot(year):
    d = df[df['year'] <= year]
    rogers = d[d['partner'] == "Mimi Rogers"]
    kidman = d[d['partner'] == "Nicole Kidman"]
    holmes = d[d['partner'] == "Katie Holmes"]
    plt.figure(figsize=(7, 4), dpi=150)
    plt.plot(d['year'], d['age'], color="orange", linewidth=2, marker='o')
    plt.bar(x=rogers['year'], height=rogers['partner_age'].fillna(0), label="Mimi Rogers")
    plt.bar(x=kidman['year'], height=kidman['partner_age'].fillna(0), label="Nicole Kidman")
    plt.bar(x=holmes['year'], height=holmes['partner_age'].fillna(0), label="Katie Holmes")
    plt.hlines(y=33, xmin=d['year'].min(), xmax=d['year'].max(), color="red")
    plt.title("Women Expire at 33 According to Tom Cruise")
    plt.xlabel("Year")
    plt.ylabel("Age")
    plt.xlim([1985, 2015])
    plt.ylim([20, 55])

frames = []
for year in range(1985, 2015+1):
    frame = plot(year)
    frames.append(frame)

gif.options.matplotlib["dpi"] = 300
gif.save(frames, "output/cruise.gif", duration=5, unit='seconds', between="startend")
