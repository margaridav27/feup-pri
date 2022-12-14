FROM solr:8.10

COPY data/sample_data.json /data/data.json
COPY data/my_synonyms.txt /data/my_synonyms.txt

COPY schemas/movie_schema.json /data/movie_schema.json

COPY ltr/config.xml /data/config.xml
COPY ltr/features.json /data/features.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
