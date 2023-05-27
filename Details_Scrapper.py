import json
import requests
import spacy
from bs4 import BeautifulSoup

from Recipe import Recipe, encode_recipe

nlp = spacy.load("en_core_web_sm")
excluded_tags = {"VERB", 'SYM', 'PUNCT', 'ADJ', 'ADP', 'CCONJ', 'PROPN'}

common_words = {"and", "minced", "peeled", "diced", "chopped", "pitted", "grated", "shredded",
                "sliced", "crushed", "mashed", "julienned", "zested", "de-seeded",
                "deveined", "cubed", "halved", "quartered", "trimmed", "husked", "whole", "dried"}


def clean_up_ingredients(s):
    print(s)
    for word in common_words:
        if word in s:
            s = s.replace(word, '')
    s = s.strip()
    return s


"""use Spacy to remove unwanted words from ingredients."""


def remove_by_type(s):
    new_sentence = []
    doc = nlp(s)
    for chunk in doc.noun_chunks:
        if chunk.text:
            new_sentence.append(clean_up_ingredients(chunk.text))
            break
    return new_sentence


"""extracts each recipe from the complete lists of urls and stores them in a JSON file
    - clean_ingredients: boolean on whether to clean up ingredients
"""


def extract_details(input_file, output_file, clean_ingredients):
    json_input = []
    infile = open(input_file, 'r', encoding='utf8')
    outfile = open(output_file, 'w', encoding='utf8')
    data = infile.readline()
    data = data.strip()
    counter = 0

    while data != '':
        data = data.strip()
        ingredients = []
        html_text = requests.get(data, allow_redirects=False).text
        soup = BeautifulSoup(html_text, 'lxml')
        ingredient_spans = soup.find_all('span', attrs={'data-ingredient-name': 'true'})
        temp_name = soup.find('h1', class_='comp type--lion article-heading mntl-text-block').text
        temp_image = soup.find('img')
        try:
            src_value = temp_image.attrs['src']
        except KeyError:
            src_value = temp_image.attrs['data-src']
        temp_name = temp_name.strip()
        if clean_ingredients:
            for ingredient in ingredient_spans:
                ingredients.append(remove_by_type(ingredient.text))
        else:
            for ingredient in ingredient_spans:
                ingredients.append(ingredient.text)
        try:
            temp_time = soup.find('div', class_='mntl-recipe-details__value').text
        except AttributeError:
            temp_time = None
        try:
            temp_rating = soup.find('div', class_='comp type-'
                                                  '-squirrel-bold mntl-recipe-review-bar__rating mntl-text-block').text
            temp_rating = temp_rating.strip()
        except AttributeError:
            temp_rating = None

        new_recipe = Recipe(counter, temp_name, ingredients, data, temp_time, temp_rating, src_value)
        json_input.append(encode_recipe(new_recipe))

        data = infile.readline()
        counter += 1

    json.dump(json_input, outfile, indent=4)
