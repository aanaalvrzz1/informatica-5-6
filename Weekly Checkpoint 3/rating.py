def main():

#variables
    rating = float(input("put your rating from 0-5: " ))

#formulas
    if rating >= 4.5:
        print("perfection")

    elif rating >= 4:
        print("excellent")

    elif rating >= 3:
        print("Good")

    elif rating >= 2:
        print("Fair")

    else:
        print("Poor")


if __name__== "__main__":
    main()
