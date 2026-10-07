def main():
    def highest(a , b):
        if a > b:
            highest_num = a
        elif b > a:
            highest_num = b
        else:
            print("Try again with other number!")

        print(f"The highest number entered is {highest_num}")

    highest(8,2)

    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))
    highest(num1,num2)

    def lowest(a ,b ,c):
        if a < b and a < c:
            lowest_num = a
        elif b < a and b < c:
            lowest_num = b
        elif c < a and c < b:
            lowest_num = c
        else:
            print("Try again with other numbers")

        print(f"The lowest number is {lowest_num} ")

    num3 = int(input("Give me a number: "))
    num4 = int(input("Give me another number: "))
    num5 = int(input("Give me another number: "))
    lowest(num3, num4, num5)

if __name__=="__main__":
    main()
