import random
def get_random_word():
    words = ["pizza", "cheese", "apples"]
    word = words[random.randint(0,len(words)-1)]
    return word

wow = get_random_word()

print wow


