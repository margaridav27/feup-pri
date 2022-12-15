#!/bin/bash

precreate-core imdb_movies

sed -i $'/<\/config>/{e cat /data/config.xml\n}' /var/solr/data/imdb_movies/conf/solrconfig.xml

# Start Solr in background mode so we can use the API to upload the schema
solr start -Dsolr.ltr.enabled=true

sleep 5

cp /data/my_synonyms.txt /var/solr/data/imdb_movies/conf/synonyms.txt

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
            --data-binary @/data/movie_schema.json \
            http://localhost:8983/solr/imdb_movies/schema

# Feature definition via API
curl -X PUT -H 'Content-type:application/json' \
             --data-binary @/data/features.json \
             http://localhost:8983/solr/imdb_movies/schema/feature-store

# Upload model for LTR
curl -X PUT -H 'Content-type:application/json' \
            --data-binary @/data/model.json \
            http://localhost:8983/solr/imdb_movies/schema/model-store

# Populate collection
bin/post -c imdb_movies /data/data.json

# Restart in foreground mode so we can access the interface
solr restart -f
