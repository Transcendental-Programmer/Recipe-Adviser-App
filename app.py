from flask import Flask, render_template, request, url_for
from recommendation_engine import recommender
import pandas as pd
import math

app = Flask(__name__, static_url_path='/static')

df = pd.read_csv('data/preprocessed_recipes.csv')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all_recipes')
def all_recipes():
    page = request.args.get('page', 1, type=int)
    per_page = 8
    total = len(df)
    pages = math.ceil(total / per_page)
    offset = (page - 1) * per_page
    recipes = df.iloc[offset:offset+per_page].to_dict('records')
    return render_template('all_recipes.html', recipes=recipes, page=page, pages=pages)

@app.route('/recipe_details/<recipe_name>')
def recipe_details(recipe_name):
    recipe = df[df['title'] == recipe_name].iloc[0].to_dict()
    return render_template('recipe_details.html', recipe=recipe)

@app.route('/test_model')
def test_model():
    return render_template('test_model.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    ingredients = request.form['ingredients'].split(',')
    similar_recipes = recommender.get_similar_recipes(ingredients)
    formatted_recipes = [recommender.format_recipe(recipe) for _, recipe in similar_recipes.iterrows()]
    return render_template('recommendations.html', recipes=formatted_recipes)

if __name__ == '__main__':
    app.run(debug=True)