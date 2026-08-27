def main():

#ask the user
    layer = input("target atmospheric layer? : ")

#if section for atmospheric layer
    if(layer == "exosphere"):
        print("your altitude level will be between 700 - 10,000 km")
    elif(layer == "thermosphere"):
        print("your altitude level will be between 85 - 700 km ")
    elif(layer == "mesosphere"):
        print("your altitude lever will be between 50 - 85 km")
    elif(layer == "stratosphere"):
        print("your altitude level will be between 12 - 50 km")
    elif(layer == "troposphere"):
        print("your altitude level will be between 0 - 12 km")
    else:
        print("ivalid response.")

#as the user exact altitude level
    altitude = float(input("enter you exact altitude level: "))

# calculation for the free fall
    if altitude == 10000:
        print()
    elif altitude >= 700:
        print()
    elif altitude >= 85:
        print()
    elif altitude >= 50:
        print()
    elif altitude >= 12:
        print()
    elif altitude >= 0:
        print()
    else:
        print("invalid number!")



if __name__=="__main__":
    main()
