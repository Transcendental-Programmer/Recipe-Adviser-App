import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
import pickle
import os

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['ingredients', 'method'])
    return df

def preprocess_text(text):
    if isinstance(text, list):
        text = ' '.join(text)
    return text.lower()

def extract_features(df):
    df['ingredients_processed'] = df['ingredients'].apply(preprocess_text)
    df['method_processed'] = df['method'].apply(preprocess_text)
    
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['ingredients_processed'] + ' ' + df['method_processed'])
    
    sentences = df['ingredients_processed'].apply(lambda x: x.split()) + df['method_processed'].apply(lambda x: x.split())
    word2vec_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
    
    return df, tfidf, tfidf_matrix, word2vec_model

def save_preprocessed_data(df, tfidf, tfidf_matrix, word2vec_model):
    os.makedirs('data', exist_ok=True)
    os.makedirs('models', exist_ok=True)

    df.to_csv('data/preprocessed_recipes.csv', index=False)
    with open('models/tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(tfidf, f)
    with open('models/tfidf_matrix.pkl', 'wb') as f:
        pickle.dump(tfidf_matrix, f)
    word2vec_model.save('models/word2vec_model.bin')

if __name__ == '__main__':
    df = load_and_clean_data('data/sanjeev_kapoor_recipes.csv')
    df, tfidf, tfidf_matrix, word2vec_model = extract_features(df)
    save_preprocessed_data(df, tfidf, tfidf_matrix, word2vec_model)
    print("Data preprocessing completed successfully!")