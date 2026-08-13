def main():
    planet = input("planet: ")

    # Separation
    print("Hello", planet)

    #Ending
    print("Hello", end=" ")
    print(planet)

    #Concatenation
    print("Hello " + planet)

    #Formatted String
    print(f"Hello {planet}")

if __name__== "__main__":
    main()
