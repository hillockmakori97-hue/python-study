# .# write a program that takes users age as input
# # if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# # if they dont have a drivers license print you are not eligible to drive
# # otherwise you are too young to drive
# 2.# Write a program that:
# # = > Takes the user's credit score and annual income as input.
# # =>If the credit score is above 700, check if the income is above 50,000:
# # =>If both conditions are met, print "Loan approved."
# # =>If only the credit score is high, print "Income requirement not met."
# # =>If the credit score is below 700, print "Credit score too

# age=input(("enter age"))
# age=int(age)
# if age>=18:
#     lis=input("Do you have a drivers license")
#     if lis=="yes":
#         res="eligible"
#     else:
#         res="ineligible"

# else:
#     res="Too young to drive"
# print(res)

# credit=input("enter your credit")
# credit=int(credit)
# income=input(("enter income"))
# income=int(income)
# if credit>700:
#     if income>50000:
#         resp="loan approved"
#     else:
#         resp="income requirement not met"
# else:
# #     resp="credit score too low"
# # print(resp)

# fruits=["mango","banana","orange"]
# for i in fruits:
#     print(i)


# list = list(range(1, 101))
# nums = []
# for n in list:
#     if n % 3 == 0 and n % 7 == 0:
#         nums.append(n)
# print(nums)

# even_numbers = []
# for i in list:
#     if i % 2 == 0:
#         even_numbers.append(i)
# print(even_numbers)

tries = 3
attempts = list(range(1, 4))

for i in attempts:
    pin = input('Enter pin:')
    correct_pin = '1234'
    if pin == correct_pin:
        print("Welcome")
        break
    else:
        remaining_tries = tries-i
        if remaining_tries > 0:
            print(f'incorrect pin try again {remaining_tries} tries remaining')
        else:
            print("account Blocked")
