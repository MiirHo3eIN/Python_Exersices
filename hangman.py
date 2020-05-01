import urllib.request
import random 
def rnd_word():
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    word_num = random.randrange(len(words))
    return words[word_num]

#logics of the game function: 
def hangman_game(trgt_word):
    #variables: 
    turns = 10
    guess_list = ""

    while len(trgt_word)>0:
        word_progress = ""
        #check the guess in the target_word
        for letters in trgt_word:
            if letters in guess_list:
                word_progress = word_progress + letters
            else: 
                word_progress = word_progress + "-" + " "    
        if word_progress == trgt_word:
            print("You win!")
            print("The secret word is: " + word_progress)
            break 
        # Handling the entered letter    
        else: 
            print("Guess Word is: " + word_progress)
            guess = input("insert a letter: ")
            if guess in guess_list:
                print("You already entered this letter.")
                guess = input("please insert another letter: ")
            elif guess.isalpha() == True: 
                guess_list = guess_list + guess 
                turns -= 1
                print("You are left with " + str(turns) + " turns to go\n")
                man_figure(turns)
            else: 
                print("please insert a letter!")
                guess = input("insert a letter: ")
            if turns == 1:
                print("Man is on his last breath\n")
            elif turns == 0:
                print("You Lost!")
                print("The true word was: " + trgt_word)
                break
        
def man_figure(turns):
    if turns == 9:
        print("  --------  \n")
    if turns == 8:
        print("  --------  ")
        print("     O      \n")
    if turns == 7:
        print("  --------  ")
        print("     O      ")
        print("     |      ")
    if turns == 6:
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    /       \n")
    if turns == 5:
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    / \     \n")
    if turns == 4:
        print("  --------  ")
        print("   \ O      ")
        print("     |      ")
        print("    / \     \n")
    if turns == 3:
        print("  --------  ")
        print("   \ O /    ")
        print("     |      ")
        print("    / \     \n")
    if turns == 2:
        print("  --------  ")
        print("    \ O /|   ")
        print("      |      ")
        print("|    / \     \n")
    if turns == 1:
        print("  --------  ")
        print("    \ O_|/   ")
        print("|     |      ")
        print("|    / \     \n")
    if turns == 0:
        print("|  -----|---  ")
        print("|     O_|    ")
        print("|    /|\     ")
        print("|    / \     \n")
                


trgt_word = rnd_word()
print("welcome to Hangman Game!")
usr_name = input("please enter your name: ")
print("welcome" , usr_name)
print("--------------------------------\n")
print("try to guess the word in less than 10 attempts")
hangman_game(trgt_word)
print()
  
        
    
    








