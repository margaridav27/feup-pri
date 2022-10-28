FROM solr:8.10

COPY data/data.csv /data/data.csv

COPY simple_schema.json /data/simple_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
