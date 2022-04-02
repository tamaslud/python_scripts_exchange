'''
Code written by Armand, modified by TamasLud
'''

guesses = 6
warnings = 3
secret_word = list("apple")
guessed_word = list("_" * len (secret_word))
guessed_chars = []

def warning_decrement(decr, warnings, guesses):
    if warnings == 0:
        guesses -= 1
    else:
        warnings -= decr
    return (warnings, guesses)

def guesses_decrement(decr, guesses):
    guesses -= decr
    if guesses == -1:
        guesses = 0
    return (guesses)

def print_hangman(guesses):
    g = "\/\/|o "
    g = (guesses)*" " + g[(guesses):]
    h = f'''
      +----+
      |    |   
      |    {g[5]} 
      |   {g[3]}{g[4]}{g[2]}
      |   {g[1]} {g[0]}
      |
    ========='''
    print (h)
    return

while guesses > 0 and guessed_word != secret_word:
    print_hangman(guesses)
    print (f"\nThe word to guess is : {' '.join(guessed_word)}")
    print (f"Guesses left: {guesses}, Warnings left: {warnings}")

    user_input = input ("Enter a letter: ").lower()[:1]
    
    if user_input.islower() == False:
        # user input is not alpha
        print ('Invalid guess enter a char from alphabet.')
        warnings, guesses = warning_decrement(1, warnings, guesses)
        continue
    
    if user_input in guessed_chars:
        # user input had been guessed
        print (f"The letter '{user_input}' had been guessed already!")
        warnings, guesses = warning_decrement(1, warnings, guesses)
        continue

    if user_input in secret_word:
        # user input is in the secret word
        guessed_chars.append(user_input)
        for index, char in enumerate (secret_word):
            if char == user_input:
                guessed_word[index] = char
    
    else:
        # user input is not in secret word
        guessed_chars.append(user_input)
        # decrement guesses by 1 if consonant, 2 if vowel
        decr = 1
        if user_input in "aeiou":
            decr = 2
        guesses = guesses_decrement(decr, guesses)


# game ends, evaluation
print()
if guessed_word == secret_word:
    print_hangman(6)
    print ("Congrats! You've guessed the secret word!")
else:
    print_hangman(guesses)
    print ("No more guesses left...")

print (f"The secret word is: '{' '.join(secret_word)}' ")
