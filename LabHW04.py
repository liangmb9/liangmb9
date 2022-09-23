# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:15:40 2022

@author: eddek
########################################################################
##
## CS 101 Lab
## Program #4
## Name Edde Kebe
## Email etk3dg@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments 
##   In The part where you ask the user if they want to play or not. Check to see what I did wrong there and give a response
########################################################################
"""

import random
def play_again() -> bool: # Function for asking user if they want to play again
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    user_input = ""
    while user_input != "N" or "No" :
        user_input = input("Do you want to play again? ==> ")
        if user_input == "Yes" or "Y":
            return True
        if user_input == "No" or "N":
            return False
        else:
            print("You must enter Y/YES/N/NO to continue.  Please try again")


def get_wager(bank: int) -> int: # This fucntion or code in this function asks player how many chips they want to wager. If number is greater than money in bank warn user if zero or less warn user
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''

    while True:
        wager_chips = int(input("How many chips do you want to wager? ==> "))
        if wager_chips <= 0:
            print("The wager amount must be greater than 0. Please enter again.")
        if wager_chips > bank:
            print("The wager amount cannot be greater that how much you have.")
        else:
            return wager_chips

def get_slot_results() -> tuple: # Code in this function returns three random integers
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)
    return reel1, reel2, reel3


def get_matches(reela, reelb, reelc) -> int: # Code in this function function is comparing integers in each reel for matches
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    
    if reela == reelb == reelc:
        return 3
    if reelc == reela != reelb or reela == reelb != reelc or reelb == reelc != reela:
        return 2
    else:
        return 0


def get_bank() -> int: # This function asks player for how many chips they want to start with if number is less than or equal zero or number is greater than 100, warn user and loop till right number is given
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    
    
    while True:
        how_many = int(input("How many chips do you want to start with ==> "))
        if how_many <= 0:
            print("Too low a value, you can only choose 1 - 100 chips")
        if how_many > 101:
            print("Too high a value, you can only choose 1-100 chips")
        else:
            return how_many
        
        
            


def get_payout(wager, matches): # Calculation for wager if some matches are made
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return 10 * wager - wager
    if matches == 2:
        return 3 * wager - wager
    if matches == 0:
        return wager * -1


if __name__ == "__main__":  # Finally, the code below if __name==__main__ is what actually outputs everything above it.

    playing = True
    while playing:
        if playing == False:
            break
        bank = get_bank()

        while bank >= 1:  # Replace with condition for if they still have money.

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
        
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
        