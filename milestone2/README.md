# Milestone 2: Running, Indexing, Retrieving

## Usage

```sh
docker build . -t imdb_movies

docker run -p 8393:8393 -d --name imdb_movies imdb_movies
```