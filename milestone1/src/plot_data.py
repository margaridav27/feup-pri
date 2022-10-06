import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("./data/final_data.csv'")

def plot_number_movies_per_year():

    # create serie to plot
    movies_year = df.groupby(df["startYear"]).count()["tconst"]

    # configure plot
    plt.rcParams.update({"font.size": 8})
    plt.ylabel("Count of movies")
    plt.title("Movies per Year")

    # create plot
    movies_year.plot.bar()

    fig = plt.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('number_movies_per_year.png')
    plt.clf()

plots = [plot_number_movies_per_year]

for i, c in enumerate(plots):
    print("Plotting: %s - %d of %d" % (c.__name__, i + 1, len(plots)))
    c()


#- movies per year
#- movies per director
#- movies per genre
#- genre per director
#- movies per duration
#- duration per genre
#- averageRating statistics
#- wordcloud synopsis
#- wordcloud title