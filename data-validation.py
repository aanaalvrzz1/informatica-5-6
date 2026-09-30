def main():

    print('You must enter a NUMBER.')
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        not_validated = True
    while not_validated:
        number = int(input('Enter a number: '))
        not_validated = False

if __name__=="__main__":
    main()
