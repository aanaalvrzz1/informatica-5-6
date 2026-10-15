#create a txt file wih alot of words.. done
#Define the main function
#Add a print("Welcome the user to the game")
#Put a random to choose a word
#add the quantity of letters in the word
#Ask the user for a letter
#store the letter in a list
#Use with..to open the TXT file
#Compare the letters of the list to the word selected
#Add a while loop for repetating the program until it guesses the word
#Add a countdown to see how mcuh mistakes he has left
#Add a if...else condition to count the chances until they are over
#If they win add a print that says ("Congrats you won!")
#If they loose add a print ("try again!")
#have a if condition that tells if the attepts are over
import random

def main():
    start_game("listofwords.txt")

def start_game(file):
    attempts = 10
    with open(file) as words:
        listwords = words.read().splitlines()
    word = random.choice(listwords).lower()
    hint = ["_"] * len(word)
    incorrect_letters = []
    while attempts > 0:
        print("Current word:", " ".join(hint))

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                break
        else:
            print("Invalid guess. Try again.")

        if guess in word and guess not in hint:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great guess!")

        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))

        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")

        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", word)
            break

    if attempts == 0 and "_" in hint:
        print("No attempts left 💀 The word was:", word)

if __name__=="__main__":
    main()

