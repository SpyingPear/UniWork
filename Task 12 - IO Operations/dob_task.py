# dob_task.py

# Open and read the DOB.txt file
with open("DOB.txt", "r") as file:
    lines = file.readlines()

# Prepare lists for names and birthdates
names = []
birthdates = []

# Separate names and birthdates
for line in lines:
    parts = line.strip().split()
    name = ' '.join(parts[:2])           # First two words are assumed to be the name
    birthdate = ' '.join(parts[2:])      # Remaining is the birthdate
    names.append(name)
    birthdates.append(birthdate)

# Print the names section
print("Name")
for name in names:
    print(name)

print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)