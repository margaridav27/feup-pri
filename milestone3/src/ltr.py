#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import subprocess

# In[2]:


QUERIES = [ 
    "http://localhost:8983/solr/imdb_movies/select?defType=dismax&fl=*%20[features]&indent=true&q.op=OR&q=christmas%5E2%20santa%5E2%20snow%20elf%20rodolf%20festive%20claus%20merry%20holliday%20%22candy%20cane%22%20%22christmas%20tree%22%20%22christmas%20eve%22%20advent&qf=originalTitle%5E1.5%20primaryTitle%5E1.5%20synopsis%5E2&tie=0.1&rows=300&rq={!ltr%20model=myModel%20efi.text={q}}",
    "http://localhost:8983/solr/imdb_movies/select?defType=dismax&fl=*%20[features]&indent=true&q.op=OR&q=space%20astronaut%20galaxy%20planets&qf=originalTitle%5E1.5%20primaryTitle%5E1.5%20synopsis%5E2&tie=0.1&rows=300&rq={!ltr%20model=myModel%20efi.text={q}}",
    "http://localhost:8983/solr/imdb_movies/select?defType=dismax&fl=*%20[features]&indent=true&q.op=OR&q=romance%20teen%5E3.0%20crush%20heart-break%5E3.0%20%22in%20love%22%5E2.0%20high-school%5E2.0%20college%20friends%20friendship%20campus%20gossip%20passion%20attraction&qf=originalTitle%5E1.5%20primaryTitle%5E1.5%20synopsis%5E2&tie=0.1&rows=300&rq={!ltr%20model=myModel%20efi.text={q}}"
]

CHRISTMAS_QRELS_FILE = "../qrels_files/christmas_movies.txt"
SPACE_QRELS_FILE = "../qrels_files/space_movies.txt"
ROMANCE_TEEN_QRELS_FILE = "../qrels_files/romance_teen.txt"

# In[3]:


info = [
    {
        "query_url": QUERIES[0],
        "qrels_file": CHRISTMAS_QRELS_FILE,
    },
    {
        "query_url": QUERIES[1],
        "qrels_file": SPACE_QRELS_FILE,
    },
    {
        "query_url": QUERIES[2],
        "qrels_file": ROMANCE_TEEN_QRELS_FILE,
    }
]

# In[4]:


modelTemplate = {
    "class": "org.apache.solr.ltr.model.LinearModel",
    "name": "myModel",
    "features": [
        { "name" : "titleLength" },
        { "name" : "synopsisLength" },
        { "name" : "rawYear" },
        { "name" : "rawRating" },
        { "name" : "rawVotes" },
        { "name" : "increment" },
        { "name" : "queryMatchTitle" },
        { "name": "queryMatchSynopsis" },
        { "name": "originalScore" }
    ],
    "params": {
        "weights": {
            "titleLength": 0,
            "synopsisLength": 0,
            "rawYear": 0,
            "rawRating": 0,
            "rawVotes": 0,
            "increment": 0,
            "queryMatchTitle": 0,
            "queryMatchSynopsis": 0,
            "originalScore": 0
        }
    }
}

# In[158]:


def extract_features(row):
    result = []
    features = row['[features]'].split(',')

    for idx, feature in enumerate(features, start=1):
        result.append(f" {idx}:{feature.split('=')[1]}")
    
    return ''.join(result)

def convert_to_dat(row, qid, relevant):
    # <line> .=. <target> qid:<qid> <feature>:<value> <feature>:<value> ... <feature>:<value> # <info>
    target = 1 if row['tconst'] in relevant else 0
    features = extract_features(row)

    return f"{target} qid:{qid}{features} # {row['tconst']}\n"

def train_model():
    args = "../ltr/svm_rank/svm_rank_learn -c 3 ../ltr/machine_learning/train.dat ../ltr/machine_learning/model"
    subprocess.run(args.split())


# In[159]:


lines = []
for idx, query_info in enumerate(info, start=1):
    relevant = list(map(lambda el: el.strip(), open(query_info['qrels_file']).readlines()))
    results = requests.get(query_info['query_url']).json()["response"]["docs"]

    df = pd.DataFrame(results)

    lines.extend(df.apply(lambda row: convert_to_dat(row, idx, relevant), axis=1))

with open("../ltr/data/train.dat", 'w') as file:
    file.writelines(lines)

# ### Train model
