import pandas as pd
import glob
import os

def readFiles(path):
    files = glob.glob(path)
    dfs = []
    for file in files:
        print(file)
        data = pd.read_json(file, typ='series')
        dfs.append(data)

    df = pd.concat(dfs, ignore_index=True)
    return df


print(os.getcwd())
df = readFiles('./jsons/C1 - 0Gkut3_1080.json')
print(df.to_markdown())


