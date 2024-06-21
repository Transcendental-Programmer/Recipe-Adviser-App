import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from unidecode import unidecode

def get_recipe_links(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    recipe_links = []
    recipe_containers = soup.find_all('div', class_="col col-sm-4 col-md-4 col-lg-4 margin_y")
    for container in recipe_containers:
        first_a_tag = container.find('a', href=True)
        if first_a_tag:
            recipe_url = first_a_tag.get('href')
            if recipe_url:
                full_recipe_url = f"https://www.sanjeevkapoor.com{recipe_url}"
                recipe_links.append(full_recipe_url)
    return recipe_links

def scrape_recipe_details(recipe_url):
    response = requests.get(recipe_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title_tag = soup.find('h1', class_='primary_font')
    title = unidecode(title_tag.text.strip()) if title_tag else 'No title found'
    
    ingredients = []
    ingredients_header = soup.find('h2', text='Ingredients')
    if ingredients_header:
        ul = ingredients_header.find_next('ul')
        if ul:
            ingredients = [unidecode(li.text.strip()) for li in ul.find_all('li')]
    
    method = []
    method_header = soup.find('h2', text='Method')
    if method_header:
        ol = method_header.find_next('ol')
        if ol:
            method = [unidecode(li.text.strip()) for li in ol.find_all('li')]
    
    table = soup.find('tbody')
    fields = ['Main ingredients', 'Cuisine', 'Course', 'Prep time', 
              'Cook time', 'Serve', 'Taste', 'Level of cooking', 'Others']
    additional_details = {field: '' for field in fields}
    
    if table:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 2:
                field_name = unidecode(cells[0].text.strip())
                field_value = unidecode(cells[1].text.strip())
                if field_name in additional_details:
                    additional_details[field_name] = field_value
    
    return {
        'title': title,
        'ingredients': ingredients,
        'method': method,
        'Main ingredients': additional_details['Main ingredients'],
        'Cuisine': additional_details['Cuisine'],
        'Course': additional_details['Course'],
        'Prep time': additional_details['Prep time'],
        'Cook time': additional_details['Cook time'],
        'Serve': additional_details['Serve'],
        'Taste': additional_details['Taste'],
        'Level of cooking': additional_details['Level of cooking'],
        'Veg/Non Veg': additional_details['Others']
    }

base_url = "https://www.sanjeevkapoor.com/Recipe?page="
total_pages = 900
all_recipe_links = []

for page in range(1, total_pages + 1):
    page_url = f"{base_url}{page}"
    print(f"Processing page {page}")
    all_recipe_links.extend(get_recipe_links(page_url))
    time.sleep(1)

all_recipe_links = list(set(all_recipe_links))
print(f"Found {len(all_recipe_links)} unique recipe links")

recipes = []
count = 1
for recipe_url in all_recipe_links:
    recipe_details = scrape_recipe_details(recipe_url)
    recipes.append(recipe_details)
    print(f"done url {count}")
    count += 1
    time.sleep(1)

print(f"Scraped {len(recipes)} recipes")

df = pd.DataFrame(recipes)
df.to_csv('sanjeev_kapoor_recipes.csv', index=False, encoding='utf-8')
