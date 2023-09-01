def remove_gallery(input_urls: str):
    """Removes unwanted gallery urls"""

    # Read all lines from the file
    with open(input_urls, 'r', encoding='utf8') as infile:
        data = infile.readlines()

    # Filter out lines that contain the word 'gallery'
    filtered_data = [item for item in data if 'gallery' not in item]

    # Write the filtered lines back to the file
    with open(input_urls, 'w', encoding='utf8') as outfile:
        outfile.writelines(filtered_data)

    infile.close()


def trim(output_urls: str, input_urls: str):
    """Trims the list of all urls down to one quarter of its original size"""

    infile = open(input_urls, 'r', encoding='utf8')
    outfile = open(output_urls, 'w', encoding='utf8')

    data = infile.readlines()
    for x in range(len(data)):
        if x % 4 == 0:
            outfile.write(data[x])

    infile.close()
    outfile.close()


