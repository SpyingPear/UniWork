user_text= input()

temp_string= ""
for x in range(len(user_text)):
    if (x%2 == 0):
        temp_string = temp_string + user_text[x].upper()
    else:
        temp_string = temp_string + user_text[x].lower()
print(temp_string)

words= user_text.split()
i = 0
for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()
final = " ".join(words)
print(final)