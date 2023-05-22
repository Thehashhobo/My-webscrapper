import requests
import Recipes_Scrapper
import Details_Scrapper

base_site = requests.get('https://www.allrecipes.com/recipes-a-z-6735880#alphabetical-list-a').text
intermediate_output_file = 'All_recipes.txt'
output_file = 'All_recipes.json'
# intermediate_output_file_test = 'small_recipes.txt'
# output_file_test = 'All_recipes_test.json'


def main():
    # Recipes_Scrapper.extract_links(intermediate_output_file, base_site)

    Details_Scrapper.extract_details(intermediate_output_file, output_file)


if __name__ == '__main__':
    main()
