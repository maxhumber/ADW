# https://www.reddit.com/r/dataisbeautiful/comments/ipx2qz/all_tom_cruises_wives_were_33_at_time_of_divorceoc/

import pandas as pd
import altair as alt
import gif

# cruise
birth_year = 1962
df = pd.DataFrame({'year': range(birth_year, 2020 + 1)})
df['age'] = df['year'] - birth_year
df['partner'] = None
df['partner_age'] = None

# rogers
df.loc[df["year"] >= 1987, "partner"] = "Mimi Rogers"
df.loc[df["year"] == 1987, "partner_age"] = 30
df.loc[df["year"] == 1988, "partner_age"] = 31
df.loc[df["year"] == 1989, "partner_age"] = 32
df.loc[df["year"] == 1990, "partner_age"] = 33

# kidman
df.loc[df["year"] >= 1991, "partner"] = "Nicole Kidman"
df.loc[df["year"] == 1991, "partner_age"] = 23
df.loc[df["year"] == 1992, "partner_age"] = 24
df.loc[df["year"] == 1993, "partner_age"] = 25
df.loc[df["year"] == 1994, "partner_age"] = 26
df.loc[df["year"] == 1995, "partner_age"] = 27
df.loc[df["year"] == 1996, "partner_age"] = 28
df.loc[df["year"] == 1997, "partner_age"] = 29
df.loc[df["year"] == 1998, "partner_age"] = 30
df.loc[df["year"] == 1999, "partner_age"] = 31
df.loc[df["year"] == 2000, "partner_age"] = 32
df.loc[df["year"] == 2001, "partner_age"] = 33

# single 1
df.loc[df["year"] >= 2002, "partner"] = None

# holmes
df.loc[df["year"] >= 2006, "partner"] = "Katie Holmes"
df.loc[df["year"] == 2006, "partner_age"] = 27
df.loc[df["year"] == 2007, "partner_age"] = 28
df.loc[df["year"] == 2008, "partner_age"] = 29
df.loc[df["year"] == 2009, "partner_age"] = 30
df.loc[df["year"] == 2010, "partner_age"] = 31
df.loc[df["year"] == 2011, "partner_age"] = 32
df.loc[df["year"] == 2012, "partner_age"] = 33

# single 2
df.loc[df["year"] >= 2013, "partner"] = None


# attempt 1
plt.figure(figsize=(10, 5))
plt.plot(df['year'], df['age'])
plt.bar(df['year'], df['partner_age'].fillna(-1))
plt.xlim([1980, 2020])
plt.ylim([20, 60])


# 2
rogers = df[df['partner'] == "Mimi Rogers"]
kidman = df[df['partner'] == "Nicole Kidman"]
holmes = df[df['partner'] == "Katie Holmes"]

plt.figure(figsize=(16, 9))
plt.bar(rogers['year'], rogers['partner_age'], color='blue')
plt.bar(kidman['year'], kidman['partner_age'], color='green')
plt.bar(holmes['year'], holmes['partner_age'], color='orange')
plt.plot(df['year'], df['age'], color="gray")
plt.scatter(df['year'], df['age'], color="gray")
plt.hlines(y=33, xmin=df['year'].min(), xmax=df['year'].max(), color="red")
plt.xlim([1980, 2020])
plt.ylim([20, 60])

#
