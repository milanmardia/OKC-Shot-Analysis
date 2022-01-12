import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv('shots_data.csv')
Adata = df[df["team"] == "Team A"]
Bdata = df[df["team"] == "Team B"]


def change(data, team):
    data["distance"] = np.sqrt(data["x"] ** 2 + data["y"] ** 2)
    data["corner"] = data["y"] <= 7.8
    iC3 = data[np.logical_and(data["corner"], abs(
        data["x"]) >= 22)]
    iNC3 = data[np.logical_and(np.logical_not(
        data["corner"]), data["distance"] >= 23.75)]
    i2PT = data[np.logical_and(np.logical_not(
        np.logical_and(data["corner"], abs(
            data["x"]) >= 22)), np.logical_not(np.logical_and(np.logical_not(
                data["corner"]), data["distance"] >= 23.75)))]

    total_shots = float(len(data))
    # ------SHOT DISTRIBUTION----------
    i2PTshotdistr = len(i2PT) / total_shots
    iNC3shotdistr = len(iNC3) / total_shots
    iC3shotdistr = len(iC3) / total_shots
    print(f'{team} 2PT shot distribution: {i2PTshotdistr}')
    print(f'{team} NC3 shot distribution: {iNC3shotdistr}')
    print(f'{team} C3 shot distribution: {iC3shotdistr}')

    # ------EFFECTIVE FG PERCENTAGE-----
    i2PTfgm = np.sum(i2PT["fgmade"])
    iNC3fgm = np.sum(iNC3["fgmade"])
    iC3fgm = np.sum(iC3["fgmade"])

    i2PTefg = 1 * i2PTfgm / len(i2PT)
    iNC3efg = 1.5 * iNC3fgm / len(iNC3)
    iC3efg = 1.5 * iC3fgm / len(iC3)

    print(f'{team} 2PT effective fg percentage: {i2PTefg}')
    print(f'{team} NC3 effective fg percentage: {iNC3efg}')
    print(f'{team} C3 effective fg percentage: {iC3efg}')

    del i2PT
    del iNC3
    del iC3


change(Adata, "Team A")
print()
change(Bdata, "Team B")

del Adata
del Bdata
del df
