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
    #exosphere
    if altitude <= 10000:
        print(round((altitude/2) + (230) + (176) + (506) + (600),1))
    #thermosphere
    elif altitude <= 700:
        print(round(altitude/2 + (176) + (506) + (600),1))
    #mesosphere
    elif altitude <= 85:
        print(round(altitude/0.2) + 506 + 600)
    #stratosphere
    elif altitude <= 50:
        print(round((altitude/0.075) + 600 ,1))
    #troposphere
    elif altitude <= 12:
        print(round((altitude/0.02 , 1)))
    else:
        print("invalid number!")



if __name__=="__main__":
    main()
