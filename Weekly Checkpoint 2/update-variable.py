def main():
    # Augmented Assignment Operator
    money = 5
    money += 10
    print(money) #this will print 15

    #substraction Assignment Operator
    minutes = 60
    minutes -= 25
    print(minutes) #this will print 35

    #multiply Assignment Operator
    skill = 10
    skill *= 2
    print(skill) #number example

    text = "ImAna"
    text *= 20
    print(text) #this prints text times the number

    #Division Assignment Operator
    pizzas = 8
    people = int(input("number of people at the pizza party: "))
    pizzas /= people
    print(pizzas) #this will print the division of the pizza and the amount of people

    # Modulus Assignment Operator
    leftover = 8
    leftover %= people
    print(leftover)




if __name__=="__main__":
    main()
