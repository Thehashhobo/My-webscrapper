import requests
import recipes_scrapper
import details_scrapper
import recipe_cleanup
import url_cleanup
"""
Initializes the web scrapping process, extracts links, details, and cleans up the data.
No Scraper API is used in this process.
"""
base_site = requests.get('https://www.allrecipes.com/recipes-a-z-6735880#alphabetical-list-a').text
intermediate_output_file = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\All_recipes_url.txt'
trimmed_output = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\trimmed_recipe_urls.txt'
output_file = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\All_recipes.json'


def main():
    recipes_scrapper.extract_links(intermediate_output_file, base_site)
    # extracts links from directory

    url_cleanup.remove_gallery(intermediate_output_file)
    # removes unwanted gallery sites

    url_cleanup.trim(trimmed_output, intermediate_output_file)
    # may need to manually insure that the number of urls in
    # trimmed_output is divisible by 5 (due to api concurrency limit)

    details_scrapper.extract_details(trimmed_output, output_file, True)
    # scrap detailed from links

    recipe_cleanup.flatten_ingredients(output_file)
    # flattens the list of ingredients

    # sometimes when this process does not work, first get the api links and use Scrap_alt


if __name__ == '__main__':
    main()
