import json


def strip_fields(input_file, output_file, specified_field):
    # Read and parse the input JSON file
    with open(input_file, 'r', encoding='utf8') as infile:
        data = [json.loads(line) for line in infile]

        # Create a new list of dictionaries containing only the specified field
        new_data = []
        for item in data:
            if specified_field in item:
                new_data.append(item[specified_field])

        # Write the new list of dictionaries to the output JSON file
        with open(output_file, 'w') as outfile:
            json.dump(new_data, outfile, indent=4)


# Example usage:
input_file = 'Food.json'
output_file = 'output.json'
specified_field = 'name'

strip_fields(input_file, output_file, specified_field)
