menu = ["Water", "tea", "biscuit", "bread"]
stock = {
    "Water": 20,
    "tea": 30,
    "biscuit": 15,
    "bread": 10
}
price = {
    "Water": 5,
    "tea": 15,
    "biscuit": 20,
    "bread": 10
}
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value
print("Total stock worth: R" + str(total_stock))