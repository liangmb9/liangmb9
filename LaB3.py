# CS 101 Lab
# Program num:
# Name: Edde Kebe
# etk3dg@umsystem.edu
# Date Created: September 15, 2022

print("Welcome to the Flarsheim Guesser!") # Welcome message will be displayed 
num = 3 # setting the number will be used to divide user input
user_in = int(input("Please think of a number between and including 1 and 100.\n")) # Asking user for their input
rem3 = user_in % num # These three steps are calculation for remainders
rem5 = user_in % 5 
rem7 = user_in % 7
#divisible_num = int(input())
while rem3 != 1000: # While remainder for user input does not equal 1000 continue to while loop
    user_input = int(input("What is the remainder when your number is divided by 3 ?")) # asking user to provide their remainder of their number divided
    if user_input < 0: # if user_input is less than zero, output below message
        print("The value entered must be 0 or greater")
    if user_input >= num: # if user input is greater than 3, output below message
        print("The value entered must be less than", num)
    if user_input == rem3:
        break

# All the steps below are similar to what I have describe above
while rem5 != 1111:
    user_input = int(input("What is the remainder when your number is divided by 5 ?"))
    if user_input < 0:
        print("The value entered must be 0 or greater")
    if user_input >= 5:
        print("The value entered must be less than 5")
    if user_input == rem5:
        break
        
while rem7 != 900:
    user_input = int(input("What is the remainder when your number is divided by 7 ?"))
    if user_input < 0:
        print("The value entered must be 0 or greater")
    if user_input >= 7:
        print("The value entered must be less than 7")
    if user_input == rem7:
        print("Your number was", user_in)
        print("How amazing is that?")
        break


# The steps down below is asking the user if they want to play again. If user enters Y, the game continue, if user enters N, the game will exit. Anything else will keep the loop going till the correct answer is inputted
choice = input("Do you want to play again? Y to continue, N to quit  ==> ")
while choice != "N":
    #choice = input("Do you want to play again? Y to continue, N to quit  ==> ")
    if choice != "Y":
        choice = input("Do you want to play again? Y to continue, N to quit  ==> ")
    elif choice == "Y":
        print("\nWelcome to the Flarsheim Guesser!\n")
        user_in = int(input("Please think of a number between and including 1 and 100.\n"))

    
    num = 3
    #user_in = int(input("Please think of a number between and including 1 and 100.\n"))
    rem3 = user_in % num
    rem5 = user_in % 5 
    rem7 = user_in % 7
    #divisible_num = int(input())
    while rem3 != 1000:
        user_input = int(input("What is the remainder when your number is divided by 3 ?"))
        if user_input < 0:
            print("The value entered must be 0 or greater")
        if user_input >= num:
            print("The value entered must be less than", num)
        if user_input == rem3:
            break
            
    while rem5 != 1111:
        user_input = int(input("What is the remainder when your number is divided by 5 ?"))
        if user_input < 0:
            print("The value entered must be 0 or greater")
        if user_input >= 5:
            print("The value entered must be less than 5")
        if user_input == rem5:
            break
            
    while rem7 != 900:
        user_input = int(input("What is the remainder when your number is divided by 7 ?"))
        if user_input < 0:
            print("The value entered must be 0 or greater")
        if user_input >= 7:
            print("The value entered must be less than 7")
        if user_input == rem7:
            print("Your number was", user_in)
            print("How amazing is that?")
            choice = input("Do you want to play again? Y to continue, N to quit  ==> ")
    
            break

