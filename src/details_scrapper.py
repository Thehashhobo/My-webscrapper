import json
import requests
import spacy
from bs4 import BeautifulSoup
import time


from Recipe import Recipe, encode_recipe

nlp = spacy.load("en_core_web_sm")
excluded_tags = {"VERB", 'SYM', 'PUNCT', 'ADJ', 'ADP', 'CCONJ', 'PROPN'}

common_words = {"and", "minced", "peeled", "diced", "chopped", "pitted", "grated", "shredded",
                "sliced", "crushed", "mashed", "julienned", "zested", "de-seeded",
                "deveined", "cubed", "halved", "quartered", "trimmed", "husked", "whole", "dried"}


def clean_up_ingredients(s: str):
    """remove unwanted words from ingredients."""
    for word in common_words:
        if word in s:
            s = s.replace(word, '')
    s = s.strip()
    return s


def remove_by_type(s: str):
    """use Spacy to remove unwanted words from ingredients."""
    new_sentence = []
    doc = nlp(s)
    for chunk in doc.noun_chunks:
        if chunk.text:
            new_sentence.append(clean_up_ingredients(chunk.text))
            break
    return new_sentence


def extract_details(input_file: str, output_file: str, clean_ingredients: bool):
    """
    extracts each recipe from the complete lists of urls and stores them in a JSON file
        - clean_ingredients: boolean on whether to clean up ingredients

    note that the number of lines in the in input file must be divisible by 5 as the input are handled in batch of 5

    """

    json_input = []
    infile = open(input_file, 'r', encoding='utf8')
    outfile = open(output_file, 'w', encoding='utf8')
    original_url = infile.readlines()
    counter = 0

    for x in range(5, len(original_url) + 1, 5):
        api_urls = []
        for i in original_url[x - 5: x]:
            r = requests.post(url='https://async.scraperapi.com/jobs',
                              json={'apiKey': '16550a1a2906130d49e61e994db77f23',
                                    'url': i})
            res = json.loads(r.text)
            api_urls.append(res.get("statusUrl"))
            print(res.get("statusUrl"))
        time.sleep(60)

        for item in api_urls:
            response_json = requests.get(item, allow_redirects=False).json()
            print(response_json.get('response', {}).get('statusCode', ''))
            if response_json.get('response', {}).get('statusCode', '') == 200:
                ingredients = []
                instructions = []
                html_text = response_json.get('response', {}).get('body', '')  # Extract HTML from the JSON

                if not html_text:  # Skip this iteration if no HTML text is found
                    print(f"Skipping URL {item} because no HTML text was found.")
                    continue

                soup = BeautifulSoup(html_text, 'lxml')
                temp_name = soup.find('h1', class_='comp type--lion article-heading mntl-text-block').text
                temp_image = soup.find('img')
                ingredient_spans = soup.find_all('span', attrs={'data-ingredient-name': 'true'})
                instructions_spans = soup.find_all('p', class_='comp mntl-sc-block mntl-sc-block-html')
                recipe_url = response_json.get('url', '')
                overview = soup.find('p', class_='comp type--dog article-subheading')

                try:
                    image_url = temp_image.attrs['src']
                    if not image_url:
                        image_url = temp_image.attrs['data-src']
                except KeyError:
                    image_url = ''
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
                                                          '-squirrel-bold mntl-recipe-review-bar_'
                                                          '_rating mntl-text-block').text
                    temp_rating = temp_rating.strip()
                except AttributeError:
                    temp_rating = None

                for steps in range(len(instructions_spans)):
                    instructions.append("step " + str(steps) + " " + str(instructions_spans[steps].text).strip('\n'))

                new_recipe = Recipe(counter, temp_name, ingredients, recipe_url,
                                    temp_time, temp_rating, image_url, instructions, overview.text.strip('\n'))
                json_input.append(encode_recipe(new_recipe))

                data = infile.readline()
                counter += 1

    json.dump(json_input, outfile, indent=4)
