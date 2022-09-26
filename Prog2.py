# -*- coding: utf-8 -*-
"""
Name: Edde Kebe
Email: etk3dg@umsystem.edu
Class Section: CS 101 Lecture
Date: 09/25/2022
Due Date: 09/25/2022

"""
import random 

print("Welcome To Two Truth And A Lie\n")
print("\nTruth or Lie??\nI enjoy coding\n")

t = "Truth"
f = "False"
num1 = random.randint(1, 2)
num2 = random.randint(1, 2)

C = "Y"
correct = 0
Incorrect = 0
while C != "N":
    print("1-",t)
    print("2-",f)
    user_answer = int(input("Choice >>>"))
    if user_answer <= 0 or user_answer >2:
        print("Invalid Input\nPlease Enter a Valid Choice")
    
    #user_answer = int(input("Choice >>>"))
    elif user_answer == num1:
        print("Correct!!\nYou got this one correct!\n")
        correct += 1
    elif user_answer == num2:
        print("Incorrect!!\nYou got this one wrong\n")
        Incorrect += 1

    print("\nTruth or Lie\nI played on a soccer team\n")
    print("1-",t)
    print("2-",f)
    user_answer = int(input("Choice >>>"))
    if user_answer == num1:
        print("Correct!!\nYou got this one correct!\n")
        correct += 1
    elif user_answer == num2:
        print("Incorrect!!\nYou got this one wrong\n")
        Incorrect += 1
        
    print("Truth or Lie??\n I like tennis.")
    print("1-",t)
    print("2-",f)
    user_answer = int(input("Choice >>>"))
    if user_answer == num1:
         print("Correct!!\nYou got this one correct!\n")
         correct += 1
    elif user_answer == num2:
        print("Incorrect!!\nYou got this one wrong\n")
        Incorrect += 1
    print(f"You got {correct} out of 3")
    break

play = input("Do you want to play again?! (Y/N)")
while play != "N":
    if play == "N" or play == "n":
        break
    elif play == "Y" or play == "y":
        while C != "N":
            print("1-",t)
            print("2-",f)
            user_answer = int(input("Choice >>>"))
            if user_answer <= 0 or user_answer >2:
                print("Invalid Input\nPlease Enter a Valid Choice")
            
            #user_answer = int(input("Choice >>>"))
            elif user_answer == num1:
                print("Correct!!\nYou got this one correct!\n")
                correct += 1
            elif user_answer == num2:
                print("Incorrect!!\nYou got this one wrong\n")
                Incorrect += 1
        
            print("\nTruth or Lie\nI played on a soccer team\n")
            print("1-",t)
            print("2-",f)
            user_answer = int(input("Choice >>>"))
            if user_answer == num1:
                print("Correct!!\nYou got this one correct!\n")
                correct += 1
            elif user_answer == num2:
                print("Incorrect!!\nYou got this one wrong\n")
                Incorrect += 1
                
            print("Truth or Lie??\n I play tennis.")
            print("1-",t)
            print("2-",f)
            user_answer = int(input("Choice >>>"))
            if user_answer == num1:
                 print("Incorrect!!\nYou got this one correct!\n")
                 Incorrect += 1
            elif user_answer == num2:
                print("Correct!!\nYou got this one right\n")
                correct += 1
            print(f"You got {correct} out of 3")
            play = input("Do you want to play again?! (Y/N)")
            break