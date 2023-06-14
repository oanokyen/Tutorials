"""
File: word_guess.py
-------------------
Word games are very popular and a great learning tool 
for both beginners and language experts.
Imagine a word game that adapts to your needs, helping you learn and practice languages with precision. 
As a French learner myself, I understand the struggle of memorizing vocabulary. 
That's why I'm determined to create a program that not only engages but also 
reinforces what you've already learned.
"""


import random


#LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game

#def choose_word_length():
#    list_words = load_dict()
#    user_inp = int(input('Enter the word length you want to play: ')) #num_chars 
#    chosen_words=[]
#    for word in list_words:
#        if len(word) == user_inp:
#            chosen_words.append(word)
#    return random.choice(chosen_words)
    
def play_game(secret_word):
    """
    This function contains the code and logic for the word game. 
    It requests for a user to guess a letter of the word for a 
    number of guesses until the word is guessed or the guesses are exhausted.
    This can be a great language learning tool and also vocabulary builder.
    """
    EXTRA_GUESSES = len(secret_word)-5  #extra guess for word length more than 5
    guess = INITIAL_GUESSES+EXTRA_GUESSES
    word_soln = "-"*len(secret_word) #initialize solution variable with all "-"s
    secret_word_loop = secret_word # to help with breaking the loop

    while True:
        user_input = str(input("Type a single letter here, then press enter: ")).upper()
        if user_input not in secret_word_loop:
            print("There are no", user_input, "'s in the word")
        for i,char in enumerate(secret_word_loop):
            if user_input == [*secret_word_loop][i]:
                print("That guess is correct")
                word_soln = [*word_soln]
                word_soln[i]=char
                word_soln="".join(word_soln)
                #print(word_soln)
                secret_word_loop= [*secret_word_loop]
                secret_word_loop[i]="-"
                secret_word_loop = "".join(secret_word_loop)
                #print(secret_word_loop)
        if user_input=="END":
            break
        guess-=1
        if guess<1 & (secret_word_loop!="-"*len(secret_word_loop)) :
            print("Sorry, you lost. The secret word was:", secret_word)
            break
        if (secret_word_loop=="-"*len(secret_word_loop)):
            print("Congratulations, the word is:",secret_word)
            break
        print("The word now looks like this: ", word_soln)
        print("You have ", guess, "guesses left")
        
        
def get_word():
    """
    This function selects a word from the loaded word list every time it is run.
    There is the added functionality of selecting the word length to play.
    """
    #index = random.randrange(3)
    #if index == 0:
    #    return 'HAPPY'
    #elif index == 1:
    #    return 'PYTHON'
    #else:
    #    return 'COMPUTER'
    list_words = load_dict()
    user_inp = int(input('Enter the word length you want to play: ')) #num_chars 
    chosen_words=[]
    for word in list_words:
        if len(word) == user_inp:
            chosen_words.append(word)
    return random.choice(chosen_words)
        
def load_dict():
    """
    This function returns a list of all words in the dictionary as specified in 
    the LEXICON_FILENAME
    """
    user_input = input("Select word game: type L for all Lexicon; type F for Top Frequency Words ").upper()
    if user_input == "F":
        FILE= "Frequency.txt"
        print("Welcome to High Frequency Word Game !")
    else:
        FILE="Lexicon.txt"
        print("Welcome to All Lexicon Word Game")
    lines=[]
    with open(FILE) as f:
        for line in f:
            line = line.strip()
            if line != "":
                lines.append(line)
        #lines = f.readlines()
        return lines

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
