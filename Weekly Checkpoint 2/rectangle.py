def main():
    width = int(input("Enter the width of the rectangle:"))
    print("O"*width)
    print("O"*width)
    print("O"*width)
    print("O"*width)
    print("O"*width)

    perimeter = (width + 5)*2
    print("this is your perimeter:", perimeter)
    area = (width*5)
    print("this is your area:",area)
    diagonal = ((5**2)+(width**2))**0.5
    print("this is your diagonal:",round(diagonal,2))





if __name__== "__main__":
    main()
