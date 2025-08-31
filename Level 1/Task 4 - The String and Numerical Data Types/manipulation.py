str_manip = input()
print(len(str_manip))
last = str_manip[-1:]
print(str_manip.replace(last,"@"))
print(str_manip[-3:][::-1])
print(str_manip[:3]+str_manip[-2:])