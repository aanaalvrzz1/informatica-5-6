def main():
    print("Welcome to this converter!")
    print("The prupose of this program is to convert a binary number to a decimal number")
    not_validated = True
    while not_validated:
        try:
            variable2 = int(input("Give me a binary number: "))
            not_validated = False
        except ValueError:
            print("Try again with a binary number!")

    binary_to_decimal()

def binary_to_decimal():
    list = ["2**0","2**1","2**2","2**3","2**4","2**5","2**6","2**7"]
    for i in range(list):
        variable = 0
        result = variable * 2 + int(variable2)
    print(result)











if __name__=="__main__":
    main()
