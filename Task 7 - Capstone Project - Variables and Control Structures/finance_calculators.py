import math
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond      - to calculate the amount you'll have to pay on a home loan.")
print("Enter either “investment” or “bond” from the menu above to proceed:")
invalid= True

while True:
    option= input().lower()
    #This asking if its investment or a bond 
    #The following are asking the questions to the investment and storing the answers
    if option == "investment": 
        invalid = False
        print("How much are you investing?")
        money= int(input())
        print("What interest rate?")
        interest_rate= int(input())
        interest_rate/=100
        print("Over how many years?")
        timespan= int(input())
        if timespan <= 0:
            invalid= True
            print("Invalid Response")
        else:
            print("Do you want “simple” or “compound” interest?" )
            interest= input()
            #this is calculating the intrest rate
            if interest == "simple":
                total= money*(1 + interest_rate * timespan)
                print(f"${total:.2f}")
            elif interest == "compound":
                total= money*math.pow((1+interest_rate),timespan)
                print(f"${total:.2f}")
                
   
    elif option == "bond" :
        invalid = False
        #This section for the option of the bond asking the question and storing the answers
        print("Value of the house")
        value= int(input())
        print("interest rate")
        interest_rate= int(input())
        interest_rate/=12
        interest_rate/=100
        print("How many months to repay?")
        months= int(input())
        if months <= 0:
            invalid= True
            print("Invalid Response")
        else:
            #This is calculating the bond time 
            repayment= (interest_rate *value)/(1-(1+interest_rate)**(-months))
            print(f"${repayment:.2f}")
        
     #This is for if they didnt choose a valid asnwer
    else:
        print("Invalid Answer")