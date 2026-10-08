def main():
    welcome()
    choice = int(input("Selcet your order: "))
    get_item(choice)

def welcome():
    menu = ["Cheeseburger","Fries","Soda","Ice Cream","Cookie"]
    print("Welcome to the restaurant!")
    print("Here is the menu:")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")


def get_item(order):
    kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    if 1 <= order <=5:
        print(kitchen[order - 1])
    else:
        print("Not in our menu. ")

#     if order == 1:
#         print("🍔")
#     elif order == 2:
#         print("🍟")
#     elif order == 3:
#         print("🥤")


if __name__=="__main__":
    main()
