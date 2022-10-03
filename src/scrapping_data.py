import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib.request

def get_synopsis(row):
    fp = urllib.request.urlopen(f'https://www.imdb.com/title/{row.tconst}/plotsummary#synopsis')
    mybytes = fp.read()
    html_doc = mybytes.decode("utf8")
    fp.close()

    soup = BeautifulSoup(html_doc, 'html.parser')
    synopsis_ul = soup.find(id='plot-synopsis-content').li

    is_empty = (synopsis_ul.p != None)


    # if empty, skip or get summaries
    if is_empty:
        summaries_ul = soup.find(id='plot-summaries-content')
        print(summaries_ul.li)
        return summaries_ul.li[0]
        return np.nan
        
    return synopsis_ul.get_text()


    

def get_pages():
    df = pd.read_csv('./data/data.csv', delimiter=';')

    df['synopsis'] = df.apply(get_synopsis, axis=1)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)
    


def main():
    get_pages()

if __name__ == "__main__":
    main()