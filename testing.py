user_text= input()

words= user_text.split()
i = 0
for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()
final = " ".join(words)
print(final)