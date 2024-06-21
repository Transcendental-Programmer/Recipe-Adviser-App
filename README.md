# Recipe Advisor

**Used web scraping to fetch 4842 recipes from SanjeevKapoor.com. Implemented word2vec and TF-IDF for ingredient parsing and similarity measurement. Provides personalized recipe recommendations based on user-input ingredients using cosine similarity.**

## Table of Contents

- [Introduction](#introduction)
- [Images](#images)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Recipe Advisor is a web application that allows users to discover delicious recipes based on the ingredients they have. By leveraging web scraping techniques and advanced NLP models, the app provides personalized recipe recommendations.

## Images

### Home Page
![Home Page](https://github.com/Transcendental-Programmer/Recipe-Adviser-App/blob/main/static/images/home.png)

### Recipe Collection
![Recipe Collection](https://github.com/Transcendental-Programmer/Recipe-Adviser-App/blob/main/static/images/all_recipes.png)

### Recipe Details
![Recipe Details](https://github.com/Transcendental-Programmer/Recipe-Adviser-App/blob/main/static/images/recipe_details.png)

### Test Model
![Test Model](https://github.com/Transcendental-Programmer/Recipe-Adviser-App/blob/main/static/images/test_model.png)

### Recommendations
![Recommendations](https://github.com/Transcendental-Programmer/Recipe-Adviser-App/blob/main/static/images/recommedations_page.png)

## Features

- Browse a collection of 4000+ recipes from SanjeevKapoor.com.
- Get personalized recipe recommendations based on user-input ingredients.
- Detailed recipe view with ingredients, method, and other details.
- Pagination for easy navigation through recipes.

## Getting Started

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Transcendental-Programmer/Recipe-Advisor-App.git
    cd recipe-advisor
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

1. Make sure you are in the project directory and the virtual environment is activated.
2. Run the Flask application:
    ```bash
    python app.py
    ```
3. Open your web browser and go to `http://127.0.0.1:5000` to access the app.

## Usage

- **Home Page:** Provides an introduction and navigation to explore recipes or test the model for personalized recommendations.
- **Explore Recipes:** Browse through the entire collection of recipes.
- **Recipe Details:** View detailed information about a specific recipe.
- **Test Model:** Enter ingredients to get personalized recipe recommendations.

## Technologies Used

- **Web Scraping:** BeautifulSoup, Requests
- **NLP Models:** word2vec, TF-IDF
- **Frameworks:** Flask, Pandas
- **Frontend:** HTML, CSS, JavaScript
- **Data Storage:** CSV files

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
