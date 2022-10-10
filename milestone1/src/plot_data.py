import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud

df = pd.read_csv("src/data.csv", delimiter=';')

df_genre = df.assign(genres=df['genres'].str.split(',')).explode('genres')

df_directors = df.assign(directors=df['directors'].str.split(',')).explode('directors')
df_directors['directors'] = df_directors['directors'].apply(lambda x: '_'.join(str(x).split(' ')))
df_directors = df_directors[df_directors['directors'] != 'nan']

def return_text(df):
    text = ''

    for idx, row in df.iterrows():
        val = str(row['synopsis'])

        tokens = val.split()

        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        text += " ".join(tokens)+" "  
    return text

def plot_number_movies_per_year():
    plt.figure(figsize=(10, 6), dpi=80)

    plt.hist(df['startYear'], color='#6C8EBF') 

    plt.ylabel('Count')
    plt.xlabel('Year')

    plt.savefig('docs/analysis/movies_per_year.png')

def plot_number_movies_per_genre():
    plt.figure(figsize=(10, 6), dpi=80)
    plt.xticks(rotation=90)

    df_genre['genres'].value_counts().plot.bar(color='#FFEB79')

    plt.ylabel('Count')
    plt.xlabel('Genre')

    plt.savefig('docs/analysis/number_movies_per_year.png')

def plot_number_adult_movies():
    plt.figure(figsize=(10, 6), dpi=80)
    df['isAdult'].value_counts().plot.bar(color='#6C8EBF')

    plt.ylabel('Count')
    plt.yscale('log')
    plt.xlabel('Adult movies')

    plt.savefig('docs/analysis/number_adult_movies.png')

def plot_number_movies_per_avg_rating():
    plt.figure(figsize=(10, 6), dpi=80)

    plt.hist(df_genre['averageRating'], color='#FFEB79')  
    plt.ylabel('Count')
    plt.xlabel('Average Rating')

    plt.savefig('docs/analysis/number_movies_per_avg_rating.png')

def plot_statistics_genres():
    df_genre.boxplot(column='averageRating', by='genres', figsize=(50,20), color='black', fontsize='35', rot='vertical')
    plt.savefig('docs/analysis/statistics_genres.png')

def plot_relation_number_votes_avg_rating():
    df.plot(kind='scatter', x='numVotes', y='averageRating', logx=True, alpha=0.7, color=['#6C8EBF'], figsize=(10,10))

    plt.ylabel('IMDB Rating')
    plt.xlabel('Number of Votes')
    plt.savefig('docs/analysis/number_votes_avg_rating.png')

def plot_directors_wordcloud():
    comment_words = ''

    for index, row in df_directors.iterrows():
        val = str(row['directors'])
        tokens = val.split()

        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens)+" "

    wordcloud = WordCloud(
        width=800, 
        height=800,
        background_color='white', 
        colormap='Set2',
        min_font_size=10).generate(comment_words)
    
    plt.figure(figsize=(8,8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)

    plt.savefig('docs/analysis/directors_wordcloud.png')

def plot_documentary_wordcloud():
    documentary = df_genre[df_genre['genres'] == 'Documentary']

    wordcloud = WordCloud(
        width=800, 
        height=800,
        background_color='white', 
        colormap='Set2',
        min_font_size=10).generate(return_text(documentary))
    
    plt.figure(figsize=(8,8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('../docs/graphics/documentary_wordcloud.png')

def plot_drama_wordcloud():
    drama = df_genre[df_genre['genres'] == 'Drama']

    wordcloud = WordCloud(
        width=800, 
        height=800,
        background_color='white', 
        colormap='Set2',
        min_font_size=10).generate(return_text(drama))
    
    plt.figure(figsize=(8,8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('../docs/graphics/drama_wordcloud.png')

def plot_comedy_wordcloud():
    comedy = df_genre[df_genre['genres'] == 'Comedy']

    wordcloud = WordCloud(
        width=800, 
        height=800,
        background_color='white', 
        colormap='Set2',
        min_font_size=10).generate(return_text(comedy))
    
    plt.figure(figsize=(8,8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('../docs/graphics/comedy_wordcloud.png')

def plot_biography_wordcloud():
    biography = df_genre[df_genre['genres'] == 'Biography']

    wordcloud = WordCloud(
        width=800, 
        height=800,
        background_color='white', 
        colormap='Set2',
        min_font_size=10).generate(return_text(biography))
    
    plt.figure(figsize=(8,8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('../docs/graphics/biography_wordcloud.png')

def plot_romance_word_cloud():
    romance = df_genre[df_genre['genres'] == 'Romance']

    wordcloud = WordCloud(
        width=800, 
        height=800,
        background_color='white', 
        colormap='Set2',
        min_font_size=10).generate(return_text(romance))
    
    plt.figure(figsize=(8,8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('../docs/graphics/romance_wordcloud.png')


plots = [
    plot_number_movies_per_year, 
    plot_number_movies_per_genre, 
    plot_number_adult_movies, 
    plot_number_movies_per_avg_rating, 
    plot_statistics_genres,
    plot_relation_number_votes_avg_rating,
    plot_documentary_wordcloud,
    plot_biography_wordcloud,
    plot_comedy_wordcloud,
    plot_drama_wordcloud,
    plot_romance_word_cloud,
    ]

for i, plot_func in enumerate(plots):
    print("Plotting: %s - %d of %d" % (plot_func.__name__, i + 1, len(plots)))
    plot_func()


