"""This is a simple Python wordgame"""
from __future__ import print_function
import random
from os import system
system('clear')

def get_random_word():
    words = ["pizza", "cheese", "apples"]
    word = words[random.randint(0,len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print (character, " ", end="")
    print ("") 

def get_guess():
    print ("Enter a letter: ")
    return raw_input()
    print("")

def process_letter(letter, secret_word, blanked_word):
    result = False 
    
    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            print("")
            blanked_word[i] = letter

    return result

def print_strikes(number_of_strikes):
    for i in range(0, number_of_strikes):
        print ('\x1b[0;33;41m' + "X " + '\x1b[0m', end="")
    print("")

def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()
    blanked_word = list("_" * len(word))

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)
        
        if not found:
            strikes +=1 
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False


    if strikes >= max_strikes:
        print ('\x1b[0;37;41m' + "Loser!" + '\x1b[0m')
        print("")
        
    else: 
        print ('\x1b[6;30;42m' + "Winner!" + '\x1b[0m')
        print("")
        

print ("Game started...")
play_word_game()

print ("Game Over")
print("")
