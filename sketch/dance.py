import pandas as pd
from matplotlib import pyplot as plt
import gif

df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
df['date'] = pd.to_datetime(df['date'])
df.loc[df.location == 'United States', 'location'] = 'USA'
df.loc[df.location == 'United Kingdom', 'location'] = 'UK'
COLOURS = {
    'China': '#550000',
    'USA': '#000055',
    'Canada': '#881111',
    'France': '#2222CC',
    'UK': '#DEDEDE'
}
df['colour'] = df['location'].map(COLOURS)
df = df[df['location'].isin([
    'USA',
    'China',
    'Canada',
    'France',
    'UK']
)]

@gif.frame
def plot_line(date):
    d = df[df['date'] <= date]
    china = d[d['location'] == 'China']
    usa = d[d['location'] == 'USA']
    plt.figure(figsize=(8, 6))
    plt.plot(china['date'], china['total_cases'], c='red')
    plt.plot(usa['date'], usa['total_cases'], c='blue')
    plt.ylim([0, 1_000_000])
    plt.title(f"COVID-19 Cases ({date.strftime('%Y-%m-%d')})", fontdict={'fontsize': 18})

dates = pd.date_range(start='2020-02-01',end=df['date'].max())
frames = []
for date in dates:
    frame = plot_line(date)
    frames.append(frame)

gif.save(frames, 'corona_line.gif', duration=100)



@gif.frame
def plot(date):
    d = df[df['date'] == date]
    d = d.sort_values('total_cases', ascending=True)
    plt.figure(figsize=(8, 6))
    plt.barh(d['location'], d['total_cases'], color=d['colour'])
    plt.xlim([0, 1_000_000])
    plt.title(f"COVID-19 Cases ({date.strftime('%Y-%m-%d')})", fontdict={'fontsize': 18})

dates = pd.date_range(start='2020-02-01',end=df['date'].max())
frames = []
for date in dates:
    frame = plot(date)
    frames.append(frame)

gif.save(frames, 'corona.gif', duration=60)




#
