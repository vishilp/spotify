from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clustered_df.csv")

def recommend_songs(song, df=df, num_rec=5):
    # Find what cluster input song belongs to and extract the cluster songs
    is_present_in_col = df['name'].isin([song]).any()
    if is_present_in_col == False:
        return "Error: Song not Found"
    song_cluster = df[df["name"] == song]["Cluster"].values[0]
    similar_songs = df[df["Cluster"] == song_cluster]

    # Extract numerical features (PCA components) from the same cluster
    pca_features = [f'PC{i+1}' for i in range(6)]#6 principal components
    cluster_features = similar_songs[pca_features].values

    # Get the feature vector of the input song
    song_index = similar_songs[similar_songs['name'] == song].index[0]
    song_vector = similar_songs.loc[song_index, pca_features].values.reshape(1, -1)

    # Compute pairwise similarity (1xN) instead of the full NxN matrix
    similarity_scores = cosine_similarity(song_vector, cluster_features)[0]

    # Get the indices of the most similar songs (excluding the input song)
    top_songs_indices = np.argsort(similarity_scores)[::-1][1:num_rec+1]

    # Retrieve recommended songs
    recommendations = similar_songs.iloc[top_songs_indices][["name", "year", "artists"]]
    recommendations = recommendations.reset_index(drop=True)
    return recommendations