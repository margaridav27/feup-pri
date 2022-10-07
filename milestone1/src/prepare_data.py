import pandas as pd

title_basics = pd.read_csv('./data/title.basics.tsv', delimiter='\t', dtype={'isAdult': object})
title_crew = pd.read_csv('./data/title.crew.tsv', delimiter='\t', dtype={'directors': str})
title_ratings = pd.read_csv('./data/title.ratings.tsv', delimiter='\t')
name_basics = pd.read_csv('./data/name.basics.tsv', delimiter='\t', dtype={'primaryName': str})


# filter by titleType

print("Filtering titles...")
title_basics = title_basics[(title_basics['titleType'] == 'movie') | (title_basics['titleType'] == 'tvMovie')]
title_basics.reset_index(inplace=True, drop=True)


# remove movies before a certain year

title_basics['startYear'] = pd.to_numeric(title_basics['startYear'], errors='coerce')
title_basics = title_basics[title_basics['startYear'] > 1990]
title_basics.reset_index(drop=True, inplace=True)

# remove movies with ratings below 7 or null values

title_ratings = title_ratings[(title_ratings['averageRating'].notnull()) & (title_ratings['averageRating'] >= 7)]
title_ratings.reset_index(inplace=True, drop=True)

# drop useless columns 

title_basics.drop(labels=['endYear', 'titleType'], axis=1, inplace=True)
title_crew.drop(labels=['writers'], axis=1, inplace=True)
title_ratings.drop(labels=['numVotes'], axis=1, inplace=True)
name_basics.drop(labels=['birthYear', 'deathYear', 'primaryProfession', 'knownForTitles'], axis=1, inplace=True)

# create dataset

print("Merging dataframes...")
df = title_basics.merge(title_crew, on='tconst', how='left').merge(title_ratings, on='tconst', how='inner')


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

print("Saving clean data to CSV file...")
df.to_csv('./processed/data.csv', index=False, sep=';')