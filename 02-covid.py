# https://www.reddit.com/r/dataisbeautiful/comments/im13tq/i_made_a_very_simple_graphic_to_show_the/g3wa56o/

import pandas as pd
from matplotlib import pyplot as plt
import gif

df = pd.read_csv(
    "data/Weekly_Counts_of_Deaths_by_State_and_Select_Causes__2019-2020.csv",
    parse_dates=[3]
)
df.columns = [c.lower().replace(" ", '_') for c in df.columns]
df = df[df['jurisdiction_of_occurrence'] == "United States"]
df = df[[
    'week_ending_date',
    'mmwr_year',
    'mmwr_week',
    "all_cause",
    'covid-19_(u071,_multiple_cause_of_death)',
    'covid-19_(u071,_underlying_cause_of_death)',
]]
df = df[df['week_ending_date'] < "2020-08-01"]
df = df.reset_index(drop=True)

# first

plt.plot(df['week_ending_date'], df['all_cause']);

# second

df19 = df[df['mmwr_year'] == 2019]
df20 = df[df['mmwr_year'] == 2020]

plt.plot(df19['mmwr_week'], df19['all_cause'])
plt.plot(df20['mmwr_week'], df20['all_cause']);

# third

plt.figure(figsize=(8, 5), dpi=100)
plt.plot(df19['mmwr_week'], df19['all_cause'],
    color="gray", linestyle='dashed', linewidth=2
)
plt.plot(df20['mmwr_week'], df20['all_cause'],
    color="red", linewidth=3
)
plt.vlines(24, 0, 100_000, color='red', linestyles='solid')
plt.ylim([0, 100_000])
plt.title("All Cause Deaths in the United States (2020)")

# fourth

week = 24
w20 = df20[df20["mmwr_week"] <= week]
max_date = w20["week_ending_date"].max()

fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
plt.plot(df19['mmwr_week'], df19['all_cause'],
    color="gray", linestyle='dashed', linewidth=2
)
plt.plot(w20['mmwr_week'], w20['all_cause'],
    color="red", linewidth=3
)
plt.vlines(week, 0, 100_000, color='black', linestyles='solid')
plt.ylim([0, 100_000])
plt.title("All Cause Deaths in the United States (2020)")
ax.set_xticks([week])
ax.set_xticklabels([f'Week {week} ({max_date.strftime("%B")})'])

# fifth

def plot(week):
    w20 = df20[df20["mmwr_week"] <= week]
    max_date = w20["week_ending_date"].max()
    fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
    plt.plot(df19['mmwr_week'], df19['all_cause'], color="gray", linestyle='dashed', linewidth=2)
    plt.plot(w20['mmwr_week'], w20['all_cause'], color="red", linewidth=3)
    plt.vlines(week, 0, 100_000, color='black')
    plt.ylim([0, 100_000])
    plt.title("All Cause Deaths in the United States (2020)")
    ax.set_xticks([week])
    ax.set_yticks(range(0, 100_000+20_000, 20_000))
    ax.set_xticklabels([f'Week {week} ({max_date.strftime("%B")})'])
    ax.set_yticklabels([0, "20K", "40K", "60K", "80K", "\n100K\nWeekly Deaths"])

plot(3)


# 6

@gif.frame
def plot(week):
    w20 = df20[df20["mmwr_week"] <= week]
    max_date = w20["week_ending_date"].max()
    fig, ax = plt.subplots(figsize=(8, 5))
    plt.plot(df19['mmwr_week'], df19['all_cause'], color="gray", linestyle='dashed', linewidth=2)
    plt.plot(w20['mmwr_week'], w20['all_cause'], color="red", linewidth=3)
    plt.vlines(week, 0, 100_000, color='black')
    plt.ylim([0, 100_000])
    plt.title("All Cause Deaths in the United States (2020)")
    ax.set_xticks([week])
    ax.set_yticks(range(0, 100_000+20_000, 20_000))
    ax.set_xticklabels([f'Week {week} ({max_date.strftime("%B")})'])
    ax.set_yticklabels([0, "20K", "40K", "60K", "80K", "\n100K\nWeekly\nDeaths"])

gif.options.matplotlib["dpi"] = 300

frames = []
for week in range(1, 30):
    frame = plot(week)
    frames.append(frame)

last_frame_x10 = [frames[-1]] * 10
frames.extend(last_frame_x10)

gif.save(frames, "output/covid.gif", duration=100)
