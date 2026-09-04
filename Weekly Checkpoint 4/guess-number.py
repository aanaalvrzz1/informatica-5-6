import random

def main():
    name = input("Hello! , What is your name? ")
    print (f"Well, {name}, I am thinking of a number between 1 and 100")
    guess = ""
    number = random.randint(1,100)

    while guess != number:
        guess = int(input("Take a guess: "))
        if guess > number:
            print("your guess is to high")
        elif guess < number:
            print("Your guess is to low ! ")
        else:
            print(f"congratulations {name}! You guessed my number!")


if __name__=="__main__":
    main()
