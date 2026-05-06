# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied

# num1=input("enter first mumber")
# num2=input("Enter second number")
# num3=input("Enter Third number")
# num1=int(num1)
# num2=int(num2)
# num3=int(num3)
# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num1 and num2>num3:
#     print(num2)
# else:
#     print(num3)

# Number1=int(input("Enter NUmber 1"))
# Number2=int(input("Enter NUmber 2"))
# Number3=int(input("Enter Number 3"))
# Number4=int(input("Enter Number 4"))
# if Number1>Number2 and Number1>Number3 and Number1>Number4:
#     print(Number1)
# elif Number2>Number1 and Number2>Number3 and Number2>Number4:
#     print(Number2)
# elif Number3>Number2 and Number3>Number4 and Number3>Number1:
#     print(Number3)
# else:
#     print(Number4)

# #Checking Balance
# Balance=input("Enter Balance:")
# Balance=int(Balance)
# if Balance<100:
#     print("Low balance")
# elif Balance>100 and Balance<1000:
#     print("Moderate Balance")
# else:
#     print("High Balance")

# number=input("Give Me a Number")
# number=float(number)
# if number<10:
#     print("Small")
# elif number<=50 and number>=10:
#     print("Medium")
# else:
#     print("large")

# Password And Email
correct_email="Admin@gmail.com"
correct_email=correct_email.lower()
correct_password="admin123"
email=(input("Enter Email : "))
password=(input("Enter password : "))
if password==correct_password and email==correct_email:
    print("Access granted")
else:
    print("Access Denied")