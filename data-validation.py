def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number: "))
            print("Number stored successfully.")
            not_validated = False 
        except ValueError:
            print("Enter an integer Number ")
if __name__=="__main__":
    main()
