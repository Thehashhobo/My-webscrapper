import json
import random
import ftfy
"""
Initializes the web scrapping process, extracts links, details, and cleans up the data.
No Scraper API is used in this process.
"""
input_file = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\All_recipes.json'
output_file = r'C:\Users\Jerry\PycharmProjects\mywebscrapper\src\data\mid_out.json'


def fix_null():
    """find all null ratings and replace them with median rating"""
    with open(input_file, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    for item in data:
        if not item['rating']:
            item['rating'] = 4

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4)

def normalize_recipe():
    """coverting all ratings to float"""
    with open(input_file, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    for r in data:
        if "rating" in r:
            r["rating"] = float(r["rating"])  

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4)  

def convert_unicode():
    """Fixes Unicode characters and removes unnecessary backslashes from 'ingredients', 'overview', and 'instructions'."""
    with open(input_file, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    for item in data:
        # Fix overview field
        if "overview" in item and isinstance(item["overview"], str):
            item["overview"] = ftfy.fix_text(item["overview"])  # ✅ Fix corrupted text
            item["overview"] = item["overview"].replace("\\", "")  # Remove backslashes

        # Fix ingredients field
        if "ingredients" in item and isinstance(item["ingredients"], list):
            item["ingredients"] = [
                ftfy.fix_text(ing).replace("\\", "") if isinstance(ing, str) else ing
                for ing in item["ingredients"]
            ]

        # Fix instructions field
        if "instructions" in item and isinstance(item["instructions"], list):
            item["instructions"] = [
                ftfy.fix_text(instr).replace("\\", "") if isinstance(instr, str) else instr
                for instr in item["instructions"]
            ]


    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)  # ensure_ascii=False keeps proper characters

def clean_url():
    """Remove unwanted characters from URLs"""
    with open(input_file, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    for item in data:
        item["url"] = item["url"].strip()

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4)

def clean_text():
    """Fix Unicode corruption in 'overview', 'ingredients', and 'instructions' by modifying the JSON file."""
    with open(input_file, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    for item in data:
        # Fix overview field
        if "overview" in item and isinstance(item["overview"], str):
            item["overview"] = ftfy.fix_text(item["overview"]).encode("utf-8", "ignore").decode("utf-8")

        # Fix ingredients field (if it's a list)
        if "ingredients" in item and isinstance(item["ingredients"], list):
            item["ingredients"] = [
                ftfy.fix_text(ing).encode("utf-8", "ignore").decode("utf-8") if isinstance(ing, str) else ing
                for ing in item["ingredients"]
            ]

        # Fix instructions field (if it's a list)
        if "instructions" in item and isinstance(item["instructions"], list):
            item["instructions"] = [
                ftfy.fix_text(instr).encode("utf-8", "ignore").decode("utf-8") if isinstance(instr, str) else instr
                for instr in item["instructions"]
            ]

    # Overwrite the existing JSON file with cleaned data
    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)  # ensure_ascii=False preserves Unicode
def main():
    # fix_null()
    # normalize_recipe()
    # convert_unicode()
    # clean_url()
    clean_text()
    
if __name__ == '__main__':
    main()
    



