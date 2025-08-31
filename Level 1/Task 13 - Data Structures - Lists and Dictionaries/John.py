incorrect_names = []
print("Enter Your Name")
while True:
    name = input().lower()
    if name == "john":
        break
    else:
        incorrect_names.append(name)
print("Incorrect names:", incorrect_names)