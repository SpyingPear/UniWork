import statistics
print("Entert 10 Numbers")
float_mumbers= []
for i in range(10):
    num= float(input())
    float_mumbers.append(num)

total = sum(float_mumbers)
print (total)

max= max(float_mumbers)
print (max)

min= min(float_mumbers)
print (min)

mean = statistics.mean((float_mumbers))
print (mean)
median= statistics.median((float_mumbers))
print (median)