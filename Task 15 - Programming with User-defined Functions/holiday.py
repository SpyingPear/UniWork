def hotel_cost(nights):
    return nights * 100

def plane_costs(city):
    if city == "Cape Town":
        return 200
    elif city == "East London":
        return 100
    elif city == "Burger Town":
        return 600
    elif city == "Cow Town":
        return 400
    else:
        return 0 
def car_rental(days):
    return days * 40
def holiday_cost(city,nights,days):
    return hotel_cost(nights) + plane_costs(city)+ car_rental(days)

city= input("Where are you going to?")
nights= int(input("How many nights will you stay?"))
days= int(input("How many days will you rent a car?"))

total= holiday_cost(city,nights,days)
print("R",total)