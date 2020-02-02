#!/usr/bin/env python3

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

# Initial state
word = 'whatever'
filled = ''.join(['_' for c in word])
guesses = set()
limbs = 6

print(grafix[6])
print('The word has', len(filled), 'letters')

while limbs > 0:
    guess = input('Your guess: ').lower()

    if len(guess) > 1 or not guess:
        print('Not a valid guess.')
        continue

    if guess in guesses:
        print('Already guessed.')
    elif guess in word:
        print('\nCorrect.')
        for i, c in enumerate(word):
            if c == guess:
                filled = filled[:i] + c + filled[i + 1:]
        print(filled, '\n')
    else:
        limbs -= 1
        print('\nWrong.', limbs, 'limbs left')
        print(grafix[limbs])

    guesses.add(guess)
    if not '_' in filled:
        print('You win.')
        break

if '_' in filled:
    print('You failed.')

print('Your guesses:', guesses)
