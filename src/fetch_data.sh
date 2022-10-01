#!/bin/bash

wget -i downloads/urls.txt -P ./downloads/ -q --show-progress && \
for file in downloads/*.gz; do gunzip $file & done