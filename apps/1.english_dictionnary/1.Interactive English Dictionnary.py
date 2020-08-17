import json

data = json.load(open("data.json"))
def word_meaning(word):
    return data[word] 


word = input("Enter word: ")

print(word_meaning(word))