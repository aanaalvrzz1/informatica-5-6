def main():

    print("Welcome to the times table quizz")
    #this values are for using them in the while loop
    not_validated = True
    not_validated2 = True

    #We start the while loop for the question 1
    while not_validated:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
            if 1 <= times_table <= 10:
                not_validated = False
        except ValueError:
            print("Enter a whole number!")

    while not_validated2:
        try:
            max_value = int(input("Enter the maximum value for your times table: "))
            if 1<= max_value <=10:
                not_validated2 = False
        except ValueError:
            print("Enter a whole number!")


        print(f"Here is your quizz on the {times_table} times table")

        for x in range(1, (max_value + 1)):
            not_validated3 = True
            answer = x * times_table
            print(f"{x} times {times_table} is: ")
            while not_validated3:
                try:
                    user_answer = int(input("The answer is? "))
                    if user_answer == answer :
                        print("correct")
                    elif user_answer != answer :
                            print("incorrect")
                    not_validated3 = False
                except ValueError:
                    print("Enter a whole number!")



if __name__ == "__main__":
    main()
