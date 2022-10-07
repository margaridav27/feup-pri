import pandas as pd

title_basics = pd.read_csv('./data/title.basics.tsv', delimiter='\t', dtype={'isAdult': object})
title_ratings = pd.read_csv('./data/title.ratings.tsv', delimiter='\t')

# filter by titleType

title_basics = title_basics[(title_basics['titleType'] == 'movie') | (title_basics['titleType'] == 'tvMovie')]
title_basics.reset_index(inplace=True, drop=True)

# remove movies before a certain year

title_basics['startYear'] = pd.to_numeric(title_basics['startYear'], errors='coerce')
title_basics = title_basics[title_basics['startYear'] > 1990]
title_basics.reset_index(drop=True, inplace=True)

# remove movies with ratings below 7 or null values

title_ratings = title_ratings[(title_ratings['averageRating'].notnull()) & (title_ratings['averageRating'] >= 7)]
title_ratings.reset_index(inplace=True, drop=True)

# save datasets

title_basics.to_csv('./data/title.basics.tsv', index=False, sep='\t')
title_ratings.to_csv('./data/title.ratings.tsv', index=False, sep='\t')