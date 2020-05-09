from gazpacho import get, Soup # pip install gazpacho
import time
from tqdm import tqdm # pip install tqdm

# parsers

def parse_tasty(soup):
    ingredients = soup.find('li', {'class': 'ingredient'}, strict=False)
    ingredients = [i.remove_tags() for i in ingredients]
    return ingredients

def parse_allrecipes(soup):
    ingredients = soup.find('span', {'class': 'recipe-ingred_txt added'})
    ingredients = [i.text for i in ingredients]
    return ingredients

def parse_ba(soup):
    ingredients = soup.find('div', {'class': 'ingredients__text'}, strict=True)
    ingredients = [i.text for i in ingredients]
    return ingredients

# actual scrape function

def url_to_ingredients(url):
    html = get(url)
    soup = Soup(html)
    if 'bonappetit.com' in url:
        ingredients = parse_ba(soup)
    elif 'allrecipes.com' in url:
        ingredients = parse_allrecipes(soup)
    elif 'tasty.co' in url:
        ingredients = parse_tasty(soup)
    else:
        raise Exception('NotAllowed')
    return ingredients

# parse an ingredient

def parse_ingredient(i):
    x = i.split(' ')
    quantity = x[0]
    unit = x[1]
    name = ' '.join(x[2:])
    return (quantity, unit), name

# run through an collate ingredients

urls = [
    'https://tasty.co/recipe/the-best-ever-vegan-brownies',
    'https://www.allrecipes.com/recipe/172367/mango-pina-colada-smoothie',
    'https://www.bonappetit.com/recipe/cucumber-tomatillo-gazpacho'
]

def url_to_parsed_ingredients(url):
    ingredients = url_to_ingredients(url)
    return [parse_ingredient(i) for i in ingredients]

grocery_list = []
for url in tqdm(urls):
    i = url_to_parsed_ingredients(url)
    grocery_list.extend(i)
    time.sleep(0.5)
