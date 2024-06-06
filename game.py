import random

#word selection
words = ['abs', 'aiter', 'all', 'anext', 'any', 'ascii', 
    'bin', 'bool', 'breakpoint', 'bytearray','bytes', 
    'callable', 'chr', 'classmethod', 'compile', 'complex', 
    'delattr', 'dict', 'dir', 'divmod',
    'enumerate', 'eval', 'exec',
    'filter', 'float', 'format', 'frozenset',
    "getattr", "globals",
    "hasattr", "hash", "help", "hex",
    "id", "input", "int", "isinstance", "issubclass", "iter",
    "len", "list", "locals",
    'map', 'max', 'memoryview', 'min', 'next',
    "object", "oct", "open", "ord",
    "pow", "print", "property",
    "range", 'repr', 'reversed', 'round', 
    'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 
    'tuple', 'type', 'vars', 'zip', '__import__'''
    ]
secret_word = random.choice(words)

#dash setup
dash = ""

for i in secret_word:
    if i != " ":
        dash += "_"
    else:
        dash += " "


the_guess = "_"
count = 0

#dash redefinition
def update_dashes(w,g,d):
    global dash
    global count
    c_update = 0
    updated = ""
    for i in range(len(w)):
        if w[i] == g:
            updated += g
            c_update += 1
        else:
            updated += d[i]
    count = c_update
    dash = updated
    return updated


def get_guess():
    print("""Welcome to [HELLO WORLD]le, the game show where we test contestents on thier python knowledge to win 10,000 dollars(worth of bragging rights). I'm your host Tracy Turtlesmith and today we're playing guess the python function. 
          At any point, if you want to solve it all, guess "final guess" """)
    global dash
    missed = []
    accurate = False
    guess_ok = False
    guess_count = 15
    while dash != secret_word and guess_count > len(secret_word):
        print("number of guesses (" + str(len(secret_word)) + " - " + str(guess_count) + "):")
        print("missed guesses: " + str(missed))
        print("guesses remaining: " + str(guess_count))
        guess = input("guess: ")
        if guess == "final guess":
            f_guess = input("final guess: ")
            dash = f_guess
            break
        elif len(guess) == 1:
            if guess.lower() == guess:
                for letter in secret_word:
                    if guess == letter:
                        accurate = True
                if accurate == True:
                    update_dashes(secret_word,guess,dash)
                    print(guess + " is in the secret word " + str(count) + " times")
                    accurate = False
                else:
                    print(guess + " is not in the secret word")
                    guess_count -= 1
                    missed.append(guess)
                guess_ok == True
            else:
                print("your guess must be a lowercase letter")
        else:
            print("your guess must have exactly one character!")
        the_guess = guess
        print(update_dashes(secret_word,guess,dash) + "(" + str(len(dash)) + " Total Characters)")
    if dash == secret_word:
      victory(True)
    else:
        victory(False)

def victory(w):
    if w == True: 
        print("congrats! You win, The word was " + secret_word)
    else:
        print("You lose. The word was: " + secret_word)
        print (""" :( (does this count as ascii art, im not an artist)""")
        

get_guess()
        
        
        
