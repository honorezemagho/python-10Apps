import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))
def word_meaning(word):
    if word in data:
        return data[word]

    elif len(get_close_matches(word,data.keys()))  >  0:
        best_match = get_close_matches(word,data.keys())[0]
        yn = input("Did you mean %s instead ? Enter Y if yes, or N if no: " % best_match)
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "Please the word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
        
    else:
        return "The word doesn't exist. Please double check it"

word_input = input("Enter word: ")

print(word_meaning(word_input.lower()))