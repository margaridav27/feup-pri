# Milestone 3: Search System

## Usage

```sh
docker build . -t imdb_movies

docker run -p 8983:8983 --name imdb_movies imdb_movies

cd milestone3/ltr/data; ../../external/svm_rank/svm_rank_learn.exe -c 5.0 train.dat model.dat
```