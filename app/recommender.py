import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

def recommender():
    df = pd.read_csv('app/static/movie_overviews.csv')
    df.dropna(subset=['title', 'overview'], inplace=True)
    df.index = np.arange(len(df))
    vec = TfidfVectorizer()
    X = vec.fit_transform(df['overview'])
    knn = NearestNeighbors(n_neighbors=10, metric='cosine').fit(X)
    
    def inner(title, nums=10, *args, **kwargs):
        overview = df.loc[df.title.str.contains(title), 'overview'].head(1)
        print(overview.empty)
        print(overview)
        if overview.empty:
            return []
        input_features = vec.transform(overview)
        distances, neighbors = knn.kneighbors(input_features, n_neighbors=nums, return_distance=True)
        print(neighbors)
        return df.title[neighbors[0]].values

    return inner