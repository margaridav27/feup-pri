import pandas as pd

title_basics = pd.read_csv('./data/title.basics.tsv', delimiter='\t', dtype={'isAdult': object})
title_crew = pd.read_csv('./data/title.crew.tsv', delimiter='\t', dtype={'directors': str})
title_ratings = pd.read_csv('./data/title.ratings.tsv', delimiter='\t')
name_basics = pd.read_csv('./data/name.basics.tsv', delimiter='\t', dtype={'primaryName': str})

# drop useless columns 

title_basics.drop(labels=['endYear', 'titleType'], axis=1, inplace=True)
title_crew.drop(labels=['writers'], axis=1, inplace=True)
name_basics.drop(labels=['birthYear', 'deathYear', 'primaryProfession', 'knownForTitles'], axis=1, inplace=True)

# save datasets

title_basics.to_csv('./data/title.basics.tsv', index=False, sep='\t')
title_crew.to_csv('./data/title.crew.tsv', index=False, sep='\t')
title_ratings.to_csv('./data/title.ratings.tsv', index=False, sep='\t')
name_basics.to_csv('./data/name.basics.tsv', index=False, sep='\t')