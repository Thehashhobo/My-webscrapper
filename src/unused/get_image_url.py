import json


def get_url(input_file: str, output_file: str):
    """flatten ingredients in recipes"""

    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')
    data = json.load(infile)

    for item in data:
        outfile.write(item.get("imagine_url").strip('\n') + '\n')

    infile.close()
    outfile.close()







