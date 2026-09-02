import random

def main():
    coin = ["heads", "tails"]
    attempts = 3
    while attempts > 0:
        flip = random.choice(coin)
        guess = input("heads or tails? ").strip().lower()

        print("The coin laned on", flip)

        if guess == flip:
            print("You Won!")
            break
        else:
            print("You Lost.")
            attempts -= 1
            print("attempts left:", attempts)

if __name__=="__main__":
    main()
