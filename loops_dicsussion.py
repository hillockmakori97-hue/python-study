# Write a program that displays a numbers 1 to 50 inside a list.
# From 1 above display the ones divisible by 7 or 5 inside a list.
# Find sum and average of values in the range between 10 to 40.
# Put in a list the first 10 odd numbers between 10 to 50. 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# # Display the total quantity of the 3 above.

list=list(range(1,51))
numbers=[]
for i in list:
    if i%7==0 or i%5==0:
        numbers.append(i)

print(numbers)

# Average
value=[]
ran=list(range(10,41))
print(ran)
total=0
count=0
for i in ran:
    total=total+i
    count=count+1
print(total)
print(count)
average=total/count
print(average)

odd=[]
lst=list(range(10,51))
for i in lst:
    if i%2!=0:
        odd.append(i)
print(odd)

numbr=int(input("Give me a number: "))
lyst=list(range(1,11))
for i in range(1,11):
    print(numbr,"x",i,"=",numbr*i)

# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
ls1=[("Jay","20"),("Mo","30"),("Mya","32")]
ls1[0]=list(ls1[0])
ls1[1]=list(ls1[1])
ls1[2]=list(ls1[2])
ls1[0][1]=int(ls1[0][1])
ls1[1][1]=int(ls1[1][1])
ls1[2][1]=int(ls1[2][1])
lts=[]
roun=0
for i in ls1:
    if type(ls1[0][1])==int and roun==0:
        lts.append(ls1[0][1])
        roun=roun+1
    elif type(ls1[1][1])==int and roun==1:
        lts.append(ls1[1][1])
        roun=roun+1
    elif type(ls1[2][1])==int and roun==2:
        lts.append(ls1[2][1])
        roun=roun+1
print(sum(lts))
