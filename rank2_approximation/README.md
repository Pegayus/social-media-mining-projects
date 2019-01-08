# Rank 2 approximation
**Caution: Running this code on a regular PC takes time!** </br>
For [movielens dataset](http://grouplens.org/datasets/movielens/) and for the top 10 movies from [imdb](http://www.imdb.com/chart/top) (movie id is in movies.csv file), I have selected all provided ratings from the movielens dataset.
First, a user-item matrix X is constructed from these ratings. It is assumed that missing ratings have value -1. A rank-2 approximation is performed on the user-item matrix. The result is plotted in a 2D space.
