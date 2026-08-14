def main():
    # planet = input("planet: ")

    # # Separation
    # print("Hello", planet)

    # #Ending
    # print("Hello", end=" ")
    # print(planet)

    # #Concatenation
    # print("Hello " + planet)

    # #Formatted String
    # print(f"Hello {planet}")

    name= input("what is your name? ").title().strip()
    color=input("Tell me a color: ").lower().strip()
    adj=input("Tell me an adjective: ").lower().strip()
    goal=input("A goal you would like to achieve: ").lower().strip()

    print()
    print("Hello", name)
    print()
    print("this is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.")
    print()

    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.".upper())



if __name__== "__main__":
    main()
