#Number Guessing Game
#ask user to guess a number
#guessed correctly then print "YOU WIN!!!!"

winning_number = 27
user_input = input ("guess a number b/w 1 and 100 : ")
user_input = input (user_input)
if user_input == winning_number:
    print("YOU WIN !!!!")
else: # nested if else
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")