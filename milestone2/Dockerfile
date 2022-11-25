FROM solr:8.10

COPY data/sample_data.json /data/data.json

COPY schemas/movie_schema.json /data/movie_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
