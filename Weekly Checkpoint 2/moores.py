def main():
    # variables
    transistors = 17.8
    years = int(input("how much years? "))
    current_year = 2026

    #operations
    if(current_year + years) >= 2030:
        print("The law is not valid.")
    else:
        transistors *= 2**(years/2)
        print("new number of transitions is:", transistors,"Billions")


if __name__=="__main__":
    main()

