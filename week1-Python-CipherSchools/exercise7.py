# ask user to input a number containing more than one digit
# example - 1234
# calculate 1+2+3+4 and print

#algorithm - (method to solve problem in human language )
#ask input in string , i.e don't change string to int 
# example - "1234"
# pick string character one by one and change to int
# int (example[0]) + int(example[1]) ...... go upto len (example) - 1

number = input ("enter a number ")
# "1234" # length = 4 , last index = 3
# int(input[i]) 
total = 0
i = 0 
while i<len(number):
    total +=int(number[i])
    i+=1
print(total)