def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number: "))
            if number >= 1 and <= 10:
                print("Number stored successfully.")
                not_validated = False
            else:
                print("That number is not between 1 and 10. Try again.")
        except ValueError:
            print("Enter an integer Number ")

    # while True:
    #     try:
    #         name = input("Enter your name: ")
    #         f_letter = name[0]
    #         print("Name stored successfully.")
    #         break
    #     except IndexError:
    #         print("A name is required.")

    name = ""
    while name = input("Enter your name: ")
        name = input("Enter your name: ")
        if name == "":
            print("A name is required.")
        else:
            print("name stored succesfully")


if __name__=="__main__":
    main()
