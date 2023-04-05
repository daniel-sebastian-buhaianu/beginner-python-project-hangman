import json
import random
from urllib.request import urlopen

URL = "https://www.randomlists.com/data/words.json"

def main():
    words = load_words(URL)
    random_index = get_random_index(words)
    print(f"Random english word: {words[random_index]}")

def load_words(url):
    json_url = urlopen(url)
    return json.loads(json_url.read())["data"]

def get_random_index(list):
    return random.randint(0, len(list) - 1)


main()