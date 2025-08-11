import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def criar_recomendador(filmes_df: pd.DataFrame):

    filmes_df['overview'] = filmes_df['overview'].fillna('')