import json


def flatten_ingredients(input_file: str):
    """flatten ingredients in recipes"""

    infile = open(input_file)
    data = json.load(infile)

    for item in data:
        item['ingredients'] = _flatten_list(item.get('ingredients'))

    with open(input_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    infile.close()
    outfile.close()


def _flatten_list(ingredients: list):
    """helper for flatten_ingredients ingredients in recipes"""

    return_list = []
    for sublist in ingredients:
        for item in sublist:
            print(item)
            return_list.append(item)
    return return_list






