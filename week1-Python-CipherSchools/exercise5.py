# WATCH COCO 
# ask user's name and age 
# If user's name start with ('a' or 'A') and age is above 10 then
# print 'you can watch coco movie'
# Else print 'sorry,you cannot watch coco'
 

user_name = input("enter your name please : " )
user_age = input ("enter your age please : ")
user_age = int(user_age)
if user_age>=10 and (user_name[0]=='a' or user_name[0] == 'A'):
    print("you can watch coco")
else:
    print("you cannot watch coco")