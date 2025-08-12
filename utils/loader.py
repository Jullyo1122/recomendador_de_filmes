import pandas as pd

def carregar_filmes(caminho="dataset/tmdb_5000_movies.csv", limite=300):
    df = pd.read_csv(caminho)
    return df.head(limite)[['title', 'overview']]


