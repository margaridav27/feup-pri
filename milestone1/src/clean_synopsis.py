import pandas as pd
import numpy as np

df = pd.read_csv('../processed/data.csv', delimiter=';')

df = df[df['synopsis'].notnull()]
df['synopsis'] = df['synopsis'].apply(lambda synopsis: synopsis.strip().replace('"', ""))

df.to_csv('data.csv', index=False, sep=';')