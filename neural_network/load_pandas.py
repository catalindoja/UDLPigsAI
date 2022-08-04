import pandas as pd
import json
import glob
import os


def readFiles(directory):
    df = pd.DataFrame()
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        data = json.load(open(file))
        df = df.append(data, ignore_index=True)

    return df


df = readFiles('./jsons/')
print(df)


