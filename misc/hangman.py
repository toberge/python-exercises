#!/usr/bin/env python3
# Only required for calling clear/cls
from os import system
from random import choice
from os.path import exists

# Some progression graphics:
grafix = [
'''
 _____
|     |
|     o
|    /|\\
|   / | \\
|    / \\
|    | |
''',
'''
 _____
|     |
|     o
|    /|\\
|   / | \\
|    / 
|    | 
''',
'''
 _____
|     |
|     o
|    /|\\
|   / | \\
|      
|      
''',
'''
 _____
|     |
|     o
|    /|
|   / | 
|      
|      
''',
'''
 _____
|     |
|     o
|     |
|     | 
|      
|      
''',
'''
 _____
|     |
|     o
|      
|       
|      
|      
''',
'''
 _____
|     |
|     
|      
|        HANGMAN 
|      
|      
'''
]

# TODO random word from http://norvig.com/ngrams/sowpods.txt or what?

if (not exists('misc/sowpods.txt')) or input('Choose a custom word? (y/N) ').startswith('y'):
    print('You curious players, hush hush!')
    word = input("It's time for the game master to decide on their word: ")
    # Prompt as long as word is not of pure alphabeticism
    if not word.replace(' ', '').isalpha():
        word = input('Please write a *normal* word: ')
else:
    with open('misc/sowpods.txt', 'r') as file:
        words = file.readlines()
    word = choice(words).strip().lower()    

# Clear screen
system('cls')
system('clear')

# Obscure all non-space characters with underscores
filled = ''.join(' ' if c == ' ' else '_' for c in word.strip())
#filled = ''.join(['_' for c in word if c != ' '])

# Set up initial state
correct = set(word)
guesses = set()
history = ''
limbs = 6

# Welcome our player(s)
print(grafix[6])
print('The word has', len(filled.replace(' ', '')), 'letters')
print(filled)
print()

# Main loop
while limbs > 0:
    guess = input('Your guess: ').lower()

    # Skip other checks if not exactly a single letter
    if len(guess) > 1 or not guess or not guess.isalpha():
        print('Not a valid guess.')
        continue

    if guess in guesses:
        print('Already guessed.')
    elif guess in correct:
        print('\nCorrect.')
        # Replace all instances of the letter in our obscured word
        for i, c in enumerate(word):
            if c == guess:
                filled = filled[:i] + c + filled[i + 1:]
        print(filled, '\n')
    else:
        # Punish the player if they made a WRONG guess
        limbs -= 1
        print('\nWrong.', limbs, 'limbs left')
        print(grafix[limbs])

    # Adding to a set --> unique
    guesses.add(guess)
    # Also saving ordered history
    history += guess

    # Testing for underscores --> win state
    if not '_' in filled:
        print('You win.')
        break

else: # Didn't exit because of win state
    print('You failed.')

print('Your guesses, in order:', ' '.join(list(history)))
print('Set of guesses:', guesses)
print('The word was:', word)
