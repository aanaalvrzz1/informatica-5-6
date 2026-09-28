def main():
    nums = []
    for i in range(1,11):
        nums.append(str(i))
    while True:
        num =(input("Enter a number (1-10) ")).lower().strip()
        if num == "exit":
            break
        elif num in nums:
            print(f"Here is the {num} times table.")
            for x in range(1,11):
                result = int(num) * x
                print(f"{x} times {num} is {result}")
        else:
            print("Invalid Command")


if __name__=="__main__":
    main()
