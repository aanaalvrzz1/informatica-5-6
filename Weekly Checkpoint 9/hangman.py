#create a txt file wih alot of words.. done
#Define the main function
#Add a print("Welcome the user to the game")
#Put a random to choose a word
#Ask the user for a letter
#store the letter in a list
#Use with..to open the TXT file
#Compare the letters of the list to the word selected
#Add a while loop for repetating the program until it guesses the word
#Add a countdown to see how mcuh mistakes he has left
#Add a if...else condition to count the chances until they are over
#If they win add a print that says ("Congrats you won!")
#If they loose add a print ("try again!")
import random
def main():
    start_game("listofwords.txt")

def start_game(letters):
    with open(letters) as words:
        listwords = words.read().splitlines()
    word = random.choice(listwords)
    print(word)

if __name__=="__main__":
    main()

