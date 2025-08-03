import pandas as pd
import ast

def carregar_filmes(caminho="dataset/tmdb_5000_movies.csv", limite=300):
    df = pd.read_csv(caminho)

    # Remove filmes sem título ou sinopse
    df = df.dropna(subset=['title', 'overview'])

    # Remove duplicatas pelo título
    df = df.drop_duplicates(subset=['title'])

    # Trata a coluna 'genres' (caso venha como string de lista de dicionários)
    if isinstance(df['genres'].iloc[0], str) and df['genres'].iloc[0].startswith("["):
        df['genres'] = df['genres'].apply(lambda x: ", ".join([g['name'] for g in ast.literal_eval(x)]))

    # Ordena por popularidade e pega os mais populares
    if 'popularity' in df.columns:
        df = df.sort_values(by='popularity', ascending=False)

    return df.head(limite)[['title', 'overview', 'genres']]
