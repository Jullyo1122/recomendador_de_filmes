import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def criar_recomendador(filmes_df: pd.DataFrame):

    filmes_df['overview'] = filmes_df['overview'].fillna('')

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(filmes_df['overview'])

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(filmes_df.index, index=filmes_df['title']).drop_duplicates()

    return cosine_sim, indices


def buscar_indice_por_titulo(titulo, indices):
    titulo = titulo.strip().lower()
    for key in indices.keys():
        if key.lower() == titulo:
            return indices[key]
    return None


def recomendar_filmes(titulo, filmes_df, cosine_sim, indices, n_recomendacoes=5):

    if titulo not in indices:
        return[]
    
    idx = indices[titulo]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:n_recomendacoes+1]

    filme_indices = [i[0] for i in sim_scores]
    
    return filmes_df['title'].iloc[filme_indices].tolist()
    