def main():

    print("Welcome to the times table quizz")
    not_validated = True
    not_validated2 = True
    not_validated3 = True
    while not_validated:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
            not_validated = False
        except ValueError:
            print("Enter a whole number!")
    while not_validated2:
        try:
            max_value = int(input("Enter a times table that you would like to be tested on: "))
            not_validated2 = False
        except ValueError:
                print("Enter a whole number!")

    if 1 <= times_table <= 10:

        print(f"Here is your quizz on the {times_table} times table")

    while not_validated3:
        for x in range(1, (max_value + 1)):
            answer = x * times_table
            print(f"{x} times {times_table} is: ")

            try:
                user_answer = int(input("The answer is?"))
                if user_answer == answer :
                    print("correct")
                elif user_answer != answer :
                    print("incorrect")
                    
            except ValueError:
                print("Enter a whole number!")




    else:
        print("Invalid command.")




if __name__ == "__main__":
    main()
