from bs4 import BeautifulSoup
import requests

"""find all links in by alphabetical list"""


def find_all_alphabet_links(soup):
    alphabet_temp = soup.find_all('div', class_='alphabetical-list__group')
    alphabet_list = []
    for alphabet in alphabet_temp:
        for link in alphabet.find_all('a'):
            alphabet_list.append(link.get('href'))
    return alphabet_list


"""find all links of sub sections grouped within each alphabetical list"""


def find_section_link(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    alphabet_temp = soup.find_all('a',
                                  class_='comp mntl-card-list-items mntl-document-card mntl-card card card--no-image')
    alphabet_list = []
    for link in alphabet_temp:
        alphabet_list.append(link.get('href'))
    return alphabet_list


"""find all links of each recipe grouped within each sub sections"""


def extract_links(output_file, base_site):
    base_soup = BeautifulSoup(base_site, 'lxml')
    all_url = []
    alphabet_list = find_all_alphabet_links(base_soup)
    for link in alphabet_list:
        all_url.extend(find_section_link(link))

    with open(output_file, 'w') as outfile:
        for item in all_url:
            if 'article' not in item:
                outfile.write(item)
                outfile.write('\n')
