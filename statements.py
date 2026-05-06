if 20>50:
    print("20 is greater")
else:
    print("20 is smaller")
    
    # Check if temperatutre is 30 ,,ptint too hot otherwise normal temperature
    temperature=30
    temp=input("enter temperature")
    temp=int(temp)

    if temp>temperature:
        print("Too hot")
    elif temp>15 and temp<30: 
        print("Normal Temperature")
    else:
        print("Too Cold")
# marks 
marks=input("Enter Marks")
marks=int(marks)
if marks>=80:
    print("A")
elif marks>=70 and marks<80:
    print("B")
elif marks>=60 and marks<70:
    print("c")
elif marks>=50 and marks<60:
    print("D")
else:
    print("E")
