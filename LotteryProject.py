#Calling modules
import plsub.inputs
import plsub.matchingandpricing

#Create variables
rand=0
uil=[]
syl=[]

#Getting inputs
for i in range (1,6):
    n=int(input("Insert number "+str(i)+" : "))
    uil.append(n)

#Displaying the inputs
plsub.inputs.getUserInputs(uil)
plsub.inputs.getSysInputs(syl)

#Matching numbers and pricing
plsub.matchingandpricing.getMatchings(uil,syl)
plsub.matchingandpricing.getPricing()

