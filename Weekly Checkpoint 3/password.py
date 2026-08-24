def main():
    #variables
    password= "InFoRmAtIc4-5-6"

    attempt= input("insert your password ")

    #formulas
    if attempt == password:
        print("You entered the pasword correctly!")
    if attempt != password:
        print("")

    print("bye!")
if __name__== "__main__":
    main()
