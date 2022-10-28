#!/bin/bash

precreate-core imdb_movies

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 10
# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
                --data-binary @/data/movie_schema.json \
                http://localhost:8983/solr/imdb_movies/schema

# Populate collection
bin/post -c imdb_movies /data/data.csv

# Restart in foreground mode so we can access the interface
solr restart -f
