#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"{self.country:15} | {self.code:10} | {self.product:20} | "
                f"R{self.cost:<8.2f} | Qty: {self.quantity}")


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip header
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    shoe = Shoe(*parts)
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    try:
        country = input("Enter country: ")
        code = input("Enter product code: ")
        product = input("Enter product name: ")
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        with open("inventory.txt", "a") as file:
            file.write(f"\n{country},{code},{product},{cost},{quantity}")
        print("Shoe added successfully.")
    except ValueError:
        print("Invalid input. Make sure cost and quantity are numbers.")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    if not shoe_list:
        print("No shoes in the list.")
        return

    print("\nAll Shoes:")
    print("-" * 75)
    for shoe in shoe_list:
        print(shoe)
    print("-" * 75)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if not shoe_list:
        print("Shoe list is empty.")
        return

    lowest = min(shoe_list, key=lambda s: s.quantity)
    print(f"\nLowest stock item:\n{lowest}")
    try:
        restock = int(input("Enter quantity to add: "))
        lowest.quantity += restock
        update_inventory_file()
        print("Stock updated.")
    except ValueError:
        print("Invalid quantity.")


def search_shoe():
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"Found:\n{shoe}")
            return
    print("Shoe not found.")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Formula: value = cost * quantity.
    '''
    if not shoe_list:
        print("No data to display.")
        return

    print("\nValue per item:")
    print("-" * 75)
    for shoe in shoe_list:
        total = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product:20} - Total Value: R{total:.2f}")
    print("-" * 75)


def highest_qty():
    '''
    Determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if not shoe_list:
        print("Shoe list is empty.")
        return

    highest = max(shoe_list, key=lambda s: s.quantity)
    print(f"\n*** FOR SALE ***\n{highest}")


def update_inventory_file():
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def main():
    read_shoes_data()

    while True:
        print("\n======= SHOE INVENTORY MENU =======")
        print("1. Add new shoe")
        print("2. View all shoes")
        print("3. Restock lowest quantity shoe")
        print("4. Search for shoe by serial number")
        print("5. Show value per item")
        print("6. Highest quality shoe for sale")
        print("7. Leave the program")
        print("===================================")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
