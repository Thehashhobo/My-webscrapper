import requests

from src import recipes_scrapper, url_cleanup, details_scrapper, scrap_from_api, recipe_cleanup
""" 
    Initializes the web scrapping process, extracts links, details, and cleans up the data.
    Scraper API is used in this process. You muse insert your API key in the details_scrapper.py file.
"""
base_site = requests.get('https://www.allrecipes.com/recipes-a-z-6735880#alphabetical-list-a').text
intermediate_output_file = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\All_recipes_url.txt'
trimmed_output = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\trimmed_recipe_urls.txt'
output_file = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\All_recipes.json'
api_storage = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\api_storage.txt'


def main():
    recipes_scrapper.extract_links(intermediate_output_file, base_site)
    # extracts links from directory

    url_cleanup.remove_gallery(intermediate_output_file)
    # removes unwanted gallery sites

    url_cleanup.trim(trimmed_output, intermediate_output_file)
    # may need to manually insure that the number of urls in
    # trimmed_output is divisible by 5 (due to api concurrency limit)

    details_scrapper.extract_details(trimmed_output, output_file, True)
    # in this case, details_scrapper generates a temporary api links file ('api_storage.txt' by default)

    scrap_from_api.extract_details(api_storage, output_file, True)

    recipe_cleanup.flatten_ingredients(output_file)
    # flattens the list of ingredients


if __name__ == '__main__':
    main()
