def main():

    #.append()
    fruits = ["apple" , "orange" , "grapes"]
    fruits.append("banana")
    print(fruits)

    #.insert()
    fruits1 = ["apple" , "orange" , "grapes"]
    fruits1.insert(2,"banana")
    print(fruits1)

    #len()
    fruits2 = ["apple" , "orange" , "grapes"]
    print(len(fruits2))

    #.sort() with numbers
    num = [1 , 5 , 8 , 3 , 4 ]
    num.sort()
    print(num)

    #.sort() in reverse
    num1 = [1 , 5 , 8 , 3 , 4 ]
    num1.sort(reverse=True)
    print(num1)

    #.sort() with a list of words
    fruits3 = ["apple" , "orange" , "grapes"]
    fruits3.sort()
    print(fruits3)

    #max
    num2 = [1 , 5 , 8 , 3 , 4 ]
    max1 = max(num2)
    print(max1)

    #min
    num3 = [1 , 5 , 8 , 3 , 4 ]
    min1 = min(num3)
    print(min1)

    #sum
    num4 = [1 , 5 , 8 , 3 , 4 ]
    sum1 = sum(num4)
    print(sum1)

    #pop
    fruits4 = ["apple" , "orange" , "grapes"]
    fruits4.pop(2)
    print(fruits4)

    #remove
    fruits5 = ["apple" , "orange" , "grapes"]
    fruits5.remove("orange")
    print(fruits5)

if __name__=="__main__":
    main()
