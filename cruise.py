# https://www.reddit.com/r/dataisbeautiful/comments/ipx2qz/all_tom_cruises_wives_were_33_at_time_of_divorceoc/

import pandas as pd

# cruise
birth_year = 1962
df = pd.DataFrame({'year': range(birth_year, 2020 + 1)})
df['age'] = df['year'] - birth_year
df['partner'] = None
df['partner_age'] = None

# rogers
df.loc[df["year"] >= 1987, "partner"] = "Mimi Rogers"
df.loc[df["year"] == 1987, "partner_age"] = 30

# kidman
df.loc[df["year"] >= 1991, "partner"] = "Nicole Kidman"
df.loc[df["year"] == 1991, "partner_age"] = 23

# single 1
df.loc[df["year"] >= 2002, "partner"] = None

# holmes
df.loc[df["year"] >= 2006, "partner"] = "Katie Holmes"
df.loc[df["year"] == 2006, "partner_age"] = 27

# single 2
df.loc[df["year"] >= 2013, "partner"] = None

age =
ages = []
for i, row in df.iterrows():
    if row.partner:
        age =
    if not df.loc[i+1, "partner_age"]:
        df.loc[i+1, "partner_age"] = row.partner_age + 1
