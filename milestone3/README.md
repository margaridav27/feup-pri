# Milestone 3: Search System

## Usage

```sh
docker build . -t imdb_movies

docker run -p 8983:8983 --name imdb_movies imdb_movies

..\..\external\svm_rank_windows\svm_rank_learn.exe -c 20.0 train.dat model.dat
```