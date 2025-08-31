total = 0
numbers = 0
average = 0
while True:
    number = int(input())
    if number == -1:
         break
    if number == 0:
         continue
    total += number
    numbers += 1
average = total / numbers
print(average)