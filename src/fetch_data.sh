#!/bin/bash

wget -i downloads/urls.txt -P ./downloads/ -q --show-progress && \
gunzip downloads/*.gz -v