from pydoc import synopsis
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib.request

def get_synopsis(row):
    print(row.tconst)
    fp = urllib.request.urlopen(f'https://www.imdb.com/title/{row.tconst}/plotsummary#synopsis')
    mybytes = fp.read()
    html_doc = mybytes.decode("utf8")
    fp.close()

    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.find(id='plot-synopsis-content'))


    

def get_pages():
    df = pd.read_csv('./data/data.csv', delimiter=';')
    #df['synopsis'] = df.head(1).apply(get_synopsis, axis=1)
    v = df.head(1).apply(get_synopsis, axis=1)


def main():
    print("Hello!")
    get_pages()

if __name__ == "__main__":
    main()