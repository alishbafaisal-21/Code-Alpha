import random

words = ["plot", "rays", "chart", "remote", "satellite"]

word = random.choice(words) # function for random word
guesses = " "
chances = 6 #chance for guessing the word

while chances >0:

    wrg_attempts=0

    for ltr in words:
        if ltr in guesses:
            print(ltr, end= " ")

        else:
            print("_", end=" ")

            wrg_attempts+=1

    if wrg_attempts==0:
        print("Congratulations! you won the game.")
        print("The word is ", {word})
        break

    print()

    guess = input("Guess the letter.")

    guesses +=guess #the store the guess letter

    if guess not in words:
        chances-=1

        print("You are failed the only left chances are ", {chances})

        if chances == 0:
            print("Game is over!")

            print("The word was", {word})












