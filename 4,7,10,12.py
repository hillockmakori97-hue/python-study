# # # task 4
# # Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# # Hint: Check if it contains an “@” symbol and “.” symbol.
# # Once you learn functions,revisit this and write this code inside a function

email=input("enter email")
def email_validate(email):
    if email.find("@")==-1 and email.find(".")==-1:
        res="missing symbol"
    return res
email_1=email_validate(email)
print(email_1)


# # # task 7
# # TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# # Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# # A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# # Once you learn functions,revisit this and write this code inside a function.






# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]
# total=0
# r=input("enter total")
# def total_stock(r):
#     for i in prods:
#         int(i[2])
#         total=i[2]+total
#     return total    
# total_may=total_stock(prods)    


# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.
# Once you learn functions,revisit this and write this code inside a function.



def largest_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        large=num1
    elif num2>num3 and num2>num3:
        large=num2
    else:
        large=num3
    return large
input1=int(input('Enter the first number:'))
input2=int(input('Enter the second number:'))
input3=int(input('Enter the third number:'))
numlarge=largest_number(input1,input2,input3)
print(numlarge)