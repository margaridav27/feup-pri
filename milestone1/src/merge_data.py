import pandas as pd

title_basics = pd.read_csv('./data/title.basics.tsv', delimiter='\t', dtype={'isAdult': object})
title_crew = pd.read_csv('./data/title.crew.tsv', delimiter='\t', dtype={'directors': str})
title_ratings = pd.read_csv('./data/title.ratings.tsv', delimiter='\t')
name_basics = pd.read_csv('./data/name.basics.tsv', delimiter='\t', dtype={'primaryName': str})

# create dataset

df = title_basics.merge(title_crew, on='tconst', how='left').merge(title_ratings, on='tconst', how='inner')

# save dataset

df.to_csv('./processed/data.csv', index=False, sep=';')