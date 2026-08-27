def main():

#variables
    n1 = int(input("give me your first number "))
    n2 = int(input("give me your second number "))
    operation = input("name of the opperation? ")

#formulas

    if operation == "multiplication":
        print(n1*n2)

    elif operation == "subtraction":
        print(n1-n2)

    elif operation == "add":
        print(n1+n2)

    else:
        print("Invalid operation.")

if __name__=="__main__":
    main()
