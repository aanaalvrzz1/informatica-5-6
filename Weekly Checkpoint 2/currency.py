def main():
    #questions
    pesos = int(input("How much do you have left in pesos?:"))
    soles = int(input("How much do you have left in soles?:"))
    reais = int(input("How much do you have left in reais?:"))

    #formulas de conversion a dolares
    pestodll = (pesos*0.00032)
    soltodll = (soles*0.30)
    reaistodll = (reais*0.19)

    #formulas de conversion a pesos y a dolares
    dolares = (pestodll+soltodll+reaistodll)
    mxn = (dolares*17.06)


    #results
    print("this is you total in dll:", round(dolares,2))
    print("this is your total in mxn:",round(mxn,2))

if __name__== "__main__":
    main()
