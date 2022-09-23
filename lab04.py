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
##
########################################################################

#import modules needed

import random


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play_again = input("Do you want to play again? ==> ")
    while play_again != "N" or "n":
        if play_again == "N" or "n":
            break
        elif play_again != "Y" or "yes" or "No" or "n":
            print("You must enter Y/Yes/N/No to continue. please try again")
        elif play_again == "Yes" or "Y":
            play_again = input("Do you want to play again? ==> ")

    return True
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    #user_input = int(input("How many chips do you start with? ==> "))
    while True:
        user_input = int(input("How many chips do you wager? ==> "))
        if user_input <= 0:
            print("The wager amount must be greater than 0. please enter again. ")
        elif user_input > bank:
            print("The wager amount cannot be greater than how much you have")
        else:
            break
        
    return 1           

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1, 11)
    reel2 = random.randint(1, 11)
    reel3 = random.randint(1, 11)
    

    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reelc:
        return 3
    elif reela == reelb or reelc:
        return 2
    elif reela != reelb or reelc:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    #user_input = int(input("How many chips do you start wager? ==> "))
    while True:
        user_input = int(input("How many chips do you want to start with? ==> "))
        if user_input <= 0:
            print("Too low a value, you can only choose 1 - 100 chips:")
        elif user_input > 100:
            print("Too high a value, you can only choose 1 - 100 chips ")
        else:
            break
    return user_input

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return (wager * 10) - wager
    elif matches == 2:
        return (wager * 2) - wager
    else:
        return (wager - wager)  


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
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