#Defining user input function
def getUserInputs(uil):
    print("\n")
    print("User numbers :",end=" ")
    for i in (uil):
        print(i,end=" ")

#Defining system input function
def getSysInputs(syl):
    import random
    print("\nLott numbers :",end=" ")
    for i in range (5):
        rand=random.randrange(1,50,2)
        print(rand, end=" ")
        syl.append(rand)
    return(syl)
