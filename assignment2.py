# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.

# def area_triangle(base,height):
#     area=0.5*base*height
#     return area
# base=int(input("entet base: "))
# height=int(input("enter height: "))
# test_area=area_triangle(base,height)
# print(test_area)

# #TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# #Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
# #Hint: how does an even / odd number react differently when divided by 2?
# #Once you learn functions,revisit this and write this code inside a function.
# #Extras:
# #If the number is a multiple of 4, print out “divisible by 4”.
# #Once you learn functions,revisit this and write this code inside a function.

test_number=input("enter number: ")
test_number=int(test_number)
def even_check(test_number):
    counter1=list(range(0,1))
    for i in counter1:
        if test_number%2==0:
            result="even"
            if test_number%4==0:
                result="divisible by 4"
        else: 
            result="odd"
        return result
example=even_check(test_number)
print(example)