# Create a list of fruits
fruits=['mango','banana','orange','lemon']
print(type(fruits))
print(fruits)
print(fruits[1])
#Update Item
fruits[1]='apple'
print(fruits)
#slice
print(fruits[2:4])
print(fruits[1:4:2])

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[::2])
numbers=[1,2,3,4,5,['alex','brian','mary',['a','b','c']],6,7,8,9,10]
print(numbers[5][1])
print(numbers[5][3][2])
