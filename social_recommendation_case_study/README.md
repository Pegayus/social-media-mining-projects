# Movie Rating Prediction
User 18 in [movielens dataset](http://grouplens.org/datasets/movielens/) has provided rating 4 for movie 858 (the godfather). This rating is set to -1 in the user-item matrix X to be predicted by using user-based and item-based CF with neighborhood size set to 5.
Next, the rank-2 approximation (Xk) of the matrix is obtained by using SVD. Xk is used to find the most similar items to 858 or users to 18 by computing cosine similarity between rows of Uk or columns of V Tk . It is assumed that the neighborhood size is 5.