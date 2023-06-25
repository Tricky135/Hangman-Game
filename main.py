import random


def welcome():
    print("""             ==================================================================================================
                    Welcome to the HANGMAN'S GAME!Please enter your preferred game name.\n""")
    name=input("Enter name:-")
    if name.isalpha()==True:
        print("""                    >>>Hi!""",name,""" glad to have you here!<<<
                    You will be playing against the computer today.
                    The computer will randomly choose a word and you will try to guess what the word is.
             ==================================================================================================
                                     Good luck!Have fun playing""")
    else:
        print('Please enter your name using letters only.')
        name=input("Enter a game name here:")
        print("Hi!",name,"Please go through the rules of the game below.")


def play_again():
    response=input("Would you like to play again?yes/no.Enter 'Y' for yes or 'N' for no\n").lower()
    if response=='y':
        game_run()
    else:
        print("Hope you had fun playing the game.See you next time.")


def get_word():
    words=['python','cool','weather','exciting','happy']
    return random.choice(words).lower()


def game_run():
    welcome()
    alphabet=('abcdefghijklmnopqrstuvwxyz')
    word=get_word()
    letters_guessed=[]
    tries=7
    guessed=False
    print()
    print("Hint!The word contains ",len(word),"letters.")
    print(len(word)*"_")

    while guessed==False and tries>0:
        print("You have"+str(tries)+"tries!")
        guess=input("Guess a letter in the word or input the full word.").lower()
        if len(guess)==1:
            if guess not in alphabet:
                print("You are to enter an alphabet not a number or special character.")
            elif guess in letters_guessed:
                print("You have guessed that letter already.Try another letter")
            elif guess not in word:
                print("Sorry,that letter is not part of the word :( ")
                letters_guessed.append(guess)
                tries-=1
            elif guess in word:
                print("Great!That letter exists in the word!")
                letters_guessed.append(guess)
            else:
                print("Check your entry!You might have entered the wrong entry")
        elif len(guess)==len(word):
            if guess==word:
                print("Great job!You guessed the word correctly!")
                guessed=True
            else:
                print("Sorry,that was not the word we were looking for :( ")
                tries-=1
        else:
            print("The length of your guess is not the same as the length of the correct word.")
            tries-=1
        status=''
        if guessed==False:
            for letter in word:
                if letter in letters_guessed:
                    status+=letter
                else:
                    status+='_'
            print(status)
        if status==word:
            print("Great job!You guessed the word correctly!")
            guessed=True
        elif tries==0:
            print("Oops!You ran out of guesses and you couldn't guess the word.")
    play_again()
game_run()