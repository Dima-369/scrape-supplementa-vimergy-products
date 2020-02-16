from bs4 import BeautifulSoup

import requests

s = requests.Session()

# Starting site with all products:
# https://www.supplementa.com/wagr/Vimergy
# note that some products are sometimes removed!
sites = [
    # Brennessel 115ml
    'https://www.supplementa.com/art/00426VY',
    # Chaga Pulver 250g
    'https://www.supplementa.com/art/00403VY',
    # Curcumin 90 capsules
    'https://www.supplementa.com/art/00413VY',
    # Ester-C 180 capsules
    'https://www.supplementa.com/art/00407VY',
    # Gerstengrassaftpulver 250g
    'https://www.supplementa.com/art/00415VY',
    # Cat's Claw 115ml
    'https://www.supplementa.com/art/00425VY',
    # L-Lysine 270 capsules
    'https://www.supplementa.com/art/00408VY',
    # Melatonin 5mg 120 capsules
    'https://www.supplementa.com/art/00422VY',
    # Reishi Pulver 250g
    'https://www.supplementa.com/art/00401VY',
    # Spirulina Pulver 250g
    'https://www.supplementa.com/art/00412VY',
    # Zink Sulfat 115ml
    'https://www.supplementa.com/art/00411VY'
]


def main():
    for site in sites:
        r = s.get(site)
        soup = BeautifulSoup(r.text, features='html.parser')
        title = soup.select_one('#description').text
        price_unit = soup.select_one('.price_unit').text \
            .replace('/', '').strip()
        # ends with a little subset 2, so we strip the last character
        shipping = soup.select_one('.availability').text \
            .strip().replace('\n', ' - ')[:-1]
        price = soup.select_one('.actualprice').text.strip()
        if 'verfügbar' in shipping:
            print(f'✓ {title} {price_unit} at {price}: {shipping}')
        else:
            print(f'    ✖ {title} {price_unit} at {price}: {shipping}')


if __name__ == '__main__':
    main()
