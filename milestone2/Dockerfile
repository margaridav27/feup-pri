FROM solr:8.10

COPY data/data.csv /data/data.csv

COPY schemas/enhanced_movie_schema.json /data/movie_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
