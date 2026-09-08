import time
def main():

    print("welcome to remember to drink your daily water! ")
    print("")
    person = input("do you consider yourself a sedentary, Moderate or a sportsman? ").strip().lower()
    weight = float(input("what is your weight(kg)? "))

    if person == "sedentary":
        total = weight * 30

    elif person == "moderate":
        total = weight * 35

    elif person == "sportsman":
        total = weight * 40

    else:
        print("that is not an option")

    print(f"you need to drink {total} ml every day " )
    print(" timer is set for every hour (8 total)")
    print(f"drink {total/5} ml every hour")


    reminder = 8
    while reminder > 0:
        print("drink water!")
        time.sleep(2)
        reminder = reminder - 1


if __name__=="__main__":
    main()
