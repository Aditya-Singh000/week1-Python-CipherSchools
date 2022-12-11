#input function

name = input("type your name ")
print("hello" + name)
age = input("what is your age? ")
print("your age is " + age) 
number_one = int(input("enter first number "))
number_two = int(input("enter second number "))
total = number_one + number_two
print("total is "+ total)

number1 = str(4)
number2 = float("44")
number3 = int("33")
print(number2 + number3)
 
#two or more input

# name = input("enter your name : ")
# age = input("enter your age : ")
name, age = input("enter your name and age").split("")
print(name)
print(age)
