import random

def main():

    guess = int(input("take a guess (1 for heads, 2 for tails): "))

    coin = random.randint(1,2)

    if coin == 1:
        print("heads")
    elif coin == 2 :
        print("tails")

    if coin == guess:
        print("you guessed")
    elif coin != guess:
        print("you lost")
    else:
        print("that is not an option")

if __name__== "__main__":
    main()

