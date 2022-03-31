#Defining matching function
def getMatchings(uil,syl):
    global mt
    n=0
    mt=0
    while (n<5):
        if (uil[n]==syl[n]):
            mt+=1
        n+=1
#Printing matches
    print("\nYou have",mt,"matches")

#Defining pricing function
def getPricing():
    if (mt==1):
        print("You Have Won Rs.50")
    elif (mt==2):
        print("You Have Won Rs.100")
    elif (mt==3):
        print("You Have Won Rs.150")
    elif (mt==4):
        print("You Have Won Rs.200")
    elif (mt==5):
        print("You Have Won Rs.250")
    else :
        print("You Haven't Won a Price")




