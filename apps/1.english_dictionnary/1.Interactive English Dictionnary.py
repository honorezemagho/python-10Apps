import json

data = json.load(open("data.json"))
def word_meaning(word):
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it"

word_input = input("Enter word: ")

print(word_meaning(word_input.lower()))