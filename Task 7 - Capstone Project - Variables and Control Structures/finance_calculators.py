import math
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond      - to calculate the amount you'll have to pay on a home loan.")
print("Enter either “investment” or “bond” from the menu above to proceed:")

option= input()
#This asking if its investment or a bond 
#The following are asking the questions to the investment and storing the answers
if option == "investment": 
    print("How much are you investing?")
    money= int(input())
    print("What interest rate?")
    interestrate= int(input())
    print("Over how many years?")
    timespan= int(input())
    print("Do you want “simple” or “compound” interest?" )
    interest= input()
    #this is calculating the intrest rate
    if interest == "simple":
        total= money*(1 + interestrate * timespan)
        print(total)
    if interest == "compound":
        total= money*math.pow((1+interestrate),timespan)
        print(total)
if option == "bond" :
    #This section for the option of the bond asking the question and storing the answers
    print("Value of the house")
    value= int(input())
    print("interest rate")
    interestrate= int(input())
    print("How many months to repay?")
    months= int(input())
    #This is calculating the bond time 
    repayment= (interestrate *value)/(1-(1+interestrate)**(-months))
    print(repayment)
#This is for if they didnt choose a valid asnwer
else:
    print("Invalid Answer")