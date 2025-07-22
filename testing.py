#Calculates the cost of the stay based off the amount of nights
def hotel_cost(nights):
    return nights * 100

# Calculates the cost of a flight based on the city
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

#Calculates the cost of the car rent based off how many days
def car_rental(days):
    return days * 40

#Calculates the total cost of the holiday
def holiday_cost(city, nights, days):
    return hotel_cost(nights) + plane_costs(city) + car_rental(days)

print("Choose a city: Cape Town, East London, Burger Town, Cow Town")
city = input("Where are you going? ").title()
nights = int(input("How many nights will you stay? "))
days = int(input("How many days will you rent a car? "))

hotel = hotel_cost(nights)
flight = plane_costs(city)
car = car_rental(days)
total = holiday_cost(city, nights, days)

#Explains to the user where the costs come from
print("\nHoliday Cost Breakdown:")
print("Hotel: R", hotel)
print("Flight: R", flight)
print("Car Rental: R", car)
print("Total: R", total)