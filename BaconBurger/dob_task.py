with open("DOB.txt", "r") as file:
    lines = file.readlines()
names = []
birthdates = []
for line in lines:
    parts = line.strip().split()
    name = ' '.join(parts[:2])           
    birthdate = ' '.join(parts[2:])      
    names.append(name)
    birthdates.append(birthdate)
print("Name")
for name in names:
    print(name)
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)