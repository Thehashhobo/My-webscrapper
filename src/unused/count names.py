import json


def count_names():
    """insures no names are too long"""

    counter = 0
    output_file = "data/All_recipes_test.json"
    with open(output_file, 'r') as outfile:
        data = json.load(outfile)
        for item in data:
            if len(item.get("name")) > 37:
                counter += 1
    return counter
