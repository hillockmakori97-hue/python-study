# Q1
# A registration portal must verify emails. Create a program that checks whether an email contains both @ and .com before accepting it.
# Q2
# A cinema only allows adults into some movies. Build a system that checks age and denies entry to anyone below 18 years.
# Q3
# A library wants automatic fines. Create a program that charges KES 20 per late day after seven allowed days.
# Q4
# A social media platform verifies popular users. Build a program that grants verification once followers exceed 10,000.
nAme=input("Enter Name: ")
email = input("enter Email: ")
email_1 = email.find(".")
email_2 = email.find("@")
if email_1 == -1 and email_2 == -1:
    print("unverified email please try again")

else:
    print("Verified Email Proceed To the Next Page")
Unconfirmed_Password = input("Enter Password: ")
confirmed_password = input("confirm password: ")
length = len(Unconfirmed_Password)
if Unconfirmed_Password==confirmed_password and len(confirmed_password)>=8 and confirmed_password[0].isupper()==True:
    password=confirmed_password
    ret=f'Success {nAme} Your Account Has Been Registered!'
else:
    ret=f'{nAme} Your registration Was Unsuccessful Please Try Again'
print(ret)



#  #cinema
name=input("Enter Name:")
age=input ("Enter Age")
age=int(age)
if age>=18:
    print(name)
    print("Access Allowed")
else:
    print("Underage not Allowed")

# # Library
Name=input("Enter Your Name:")
book_id=input("Enter book name:")
days_borrowed=input("enter number of days: ")
days_borrowed=int(days_borrowed)
if days_borrowed>7:
    delay=(days_borrowed)-7
    fine=(delay)*20
    message=f'Hey {Name} you have exceeded seven days hence artacting a fine of ksh{fine}'
else:
    message=f'Hey {Name} no fine thank you for returning the book on time'
print(message)

# # Verified Badge
user_name=input("Enter User_name: ")
followers=input("Enter Followers: ")
followers=int(followers)
if followers>=10000:
    print(user_name)
    print("verified User")
else:
    print(user_name)
    print("unverified user")
