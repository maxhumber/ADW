from gazpacho import get, Soup # pip install gazpacho

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

# testing sandbox
import time

urls = [
    'https://www.bonappetit.com/recipe/vegetarian-green-curry',
    'https://www.bonappetit.com/recipe/banana-bread',
    'https://www.allrecipes.com/recipe/45688/coconut-curry-tofu/',
    'https://www.allrecipes.com/recipe/172367/mango-pina-colada-smoothie',
    'https://tasty.co/recipe/dutch-oven-jalapeno-cheddar-bread',
    'https://tasty.co/recipe/the-best-ever-vegan-brownies',
]

from tqdm import tqdm # pip install tqdm

for url in tqdm(urls):
    print(url_to_ingredients(url))
    time.sleep(0.5)

# test on parsing

url = 'https://www.bonappetit.com/recipe/cucumber-tomatillo-gazpacho'







#
