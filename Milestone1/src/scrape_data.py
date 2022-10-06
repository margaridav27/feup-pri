import pandas as pd
import numpy as np
from tqdm import tqdm
from bs4 import BeautifulSoup
import urllib.request

def get_synopsis(row):
    fp = urllib.request.urlopen(f'https://www.imdb.com/title/{row.tconst}/plotsummary#synopsis')
    mybytes = fp.read()
    html_doc = mybytes.decode("utf8")
    fp.close()

    soup = BeautifulSoup(html_doc, 'html.parser')
    synopsis_ul = soup.find(id='plot-synopsis-content').li

    # if empty, skip or get summaries
    if synopsis_ul.get('id') == 'no-synopsis-content':
        summaries_ul = soup.find(id='plot-summaries-content').li
        return np.nan if (summaries_ul.get('id') == 'no-summary-content') else summaries_ul.get_text()
        
    return synopsis_ul.get_text()

tqdm.pandas()
df = pd.read_csv('./processed/data.csv', delimiter=';')

print("Scraping synopsis...")
try:
    df['synopsis'] = df.progress_apply(get_synopsis, axis=1)
except Exception as e:
    print('ERROR: ', e)
finally:
    df.to_csv('./data/final_data.csv', index=False, sep=';')


print("Saving final data to CSV file...")
df.to_csv('./processed/final_data.csv', index=False, sep=';')
