import json, random, string
from urllib.request import urlopen


URL = "https://www.randomlists.com/data/words.json"

def get_random_word():
    json_url = urlopen(URL)
    words = json.loads(json_url.read())["data"]
    return random.choice(words)

def hangman():
    word = get_random_word().upper()
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting the user input
    while len(word_letters) > 0:
        # letters used
        # ' '.join(["a", "b", "cd"]) -> "a b cd"
        print("You have used these letters: ", ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]

        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again")

        else:
            print("Invalid. Please try again")

    print(f"Yay, you guessed the word {word} !")


# Run hangman
hangman()