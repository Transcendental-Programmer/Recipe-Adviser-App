import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from gensim.models import Word2Vec

class RecipeRecommender:
    def __init__(self):
        self.df = None
        self.tfidf = None
        self.tfidf_matrix = None
        self.word2vec_model = None

    def load_models(self):
        self.df = pd.read_csv('data/preprocessed_recipes.csv')
        with open('models/tfidf_vectorizer.pkl', 'rb') as f:
            self.tfidf = pickle.load(f)
        with open('models/tfidf_matrix.pkl', 'rb') as f:
            self.tfidf_matrix = pickle.load(f)
        self.word2vec_model = Word2Vec.load('models/word2vec_model.bin')

    def get_recipe_vector(self, ingredients):
        ingredients_text = ' '.join(ingredients)
        ingredients_vector = self.tfidf.transform([ingredients_text])
        return ingredients_vector

    def get_similar_recipes(self, ingredients, n=5):
        ingredients_vector = self.get_recipe_vector(ingredients)
        similarities = cosine_similarity(ingredients_vector, self.tfidf_matrix)
        similar_indices = similarities.argsort()[0][-n:][::-1]
        similar_recipes = self.df.iloc[similar_indices]
        return similar_recipes

    def format_recipe(self, recipe):
        method_steps = recipe['method']
        if isinstance(method_steps, str):
            method_steps = eval(method_steps)
        formatted_method = [f"{i+1}. {step}" for i, step in enumerate(method_steps)]
        
        return {
            'title': recipe['title'],
            'ingredients': recipe['ingredients'],
            'method': formatted_method,
            'main_ingredients': recipe['Main ingredients'],
            'cuisine': recipe['Cuisine'],
            'course': recipe['Course'],
            'prep_time': recipe['Prep time'],
            'cook_time': recipe['Cook time'],
            'serve': recipe['Serve'],
            'taste': recipe['Taste'],
            'level_of_cooking': recipe['Level of cooking'],
            'veg_non_veg': recipe['Veg/Non Veg']
        }

recommender = RecipeRecommender()
recommender.load_models()

print("Models loaded successfully!")