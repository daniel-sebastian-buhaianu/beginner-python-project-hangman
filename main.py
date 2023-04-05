import json
import random
from urllib.request import urlopen

URL = "https://www.randomlists.com/data/words.json"

def main():
    words = load_words(URL)
    print(f"Random english word: {random.choice(words)}")

def load_words(url):
    json_url = urlopen(url)
    return json.loads(json_url.read())["data"]

main()