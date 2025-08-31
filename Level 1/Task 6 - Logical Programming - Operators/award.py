Swimming= int(input())
cycling= int(input())
running= int(input())
total = (running+Swimming+cycling)
if total <= 100 :
    print ("Provincial colours")
elif total<= 105 :
    print("Provincial half colours")
elif total<= 106 :
    print("Provincial scroll")
elif total> 111:
    print("No award")