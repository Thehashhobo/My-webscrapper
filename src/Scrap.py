import requests
import recipes_scrapper
import details_scrapper
import url_cleanup

base_site = requests.get('https://www.allrecipes.com/recipes-a-z-6735880#alphabetical-list-a').text
intermediate_output_file = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\All_recipes_url.txt'
trimmed_output = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\trimmed_recipe_urls.txt'
# test = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\trimmed_text.txt'
output_file = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\All_recipes.json'


def main():
    #    recipes_scrapper.extract_links(intermediate_output_file, base_site)
    #    url_cleanup.remove_gallery(intermediate_output_file)
    #    url_cleanup.trim(trimmed_output, intermediate_output_file)
    # may need to manually insure that the number of urls in trimmed_output is divisible by 5
    details_scrapper.extract_details(trimmed_output, output_file, True)


if __name__ == '__main__':
    main()
