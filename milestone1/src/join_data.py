from typing import final
import pandas as pd
import numpy as np

df = pd.read_csv('../processed/data.csv', delimiter=';')
df_synopsis = pd.read_csv('../processed/final_data.csv', delimiter=';')

final_df = df.merge(df_synopsis, on='tconst', how='left')
final_df = final_df[final_df['synopsis'] != np.nan]

final_df.to_csv('data.csv', index=False, sep=';')