file = open("DOB.txt", "r")
names = []
birthdates = []
for line in file:
    parts = line.strip().split()
    name = parts[0] + " " + parts[1]
    birthdate = parts[2] + " " + parts[3] + " " + parts[4]
    names.append(name)
    birthdates.append(birthdate)
file.close()
print("Name")
for name in names:
    print(name)
print("\nBirthdate")
for date in birthdates:
    print(date)
