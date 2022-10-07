import pandas as pd

name_basics = pd.read_csv('./data/name.basics.tsv', delimiter='\t', dtype={'primaryName': str})
df = pd.read_csv('./processed/data.csv', delimiter=';')

# explode movie rows with more than one director into multiple rows, each one with only one director code

df = df.assign(directors=df['directors'].str.split(',')).explode('directors')
df = df.merge(name_basics, left_on='directors', right_on='nconst', how='left')

# drop useless columns

df.drop(labels=['directors', 'nconst'], axis=1, inplace=True)
df.rename(columns={'primaryName' : 'directors'}, inplace=True)

# remove duplicate rows while joining director names

df['directors'] = df['directors'].astype(str)
directors_column = df.groupby(['tconst']).agg({'directors': ', '.join})['directors'].values

df.drop_duplicates(subset='tconst', inplace=True)
df['directors'] = directors_column

# save dataset

df.to_csv('./processed/data.csv', index=False, sep=';')