
def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("how", "why","what", "Hwo", "Why", "What")
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


user_words = []
while True:
    user_input = input("Say Something: ")
    if user_input == '\end':
        print(" ".join(user_words))
        break
    else:
        user_words.append(sentence_maker(user_input))
        continue