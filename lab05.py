########################################################################
##
## CS 101 Lab
## Program #5
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


# import statement
import string
# functions
hall = "Linda Hall"
#print(f"'                    '{hall}")
#print("==========================================================")

def get_school(str1):
    
    if (1*int(str1[5])+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10 == (1*1+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10: # If str1 value equal the value those calculated numbers return School of Computing and Engineering SCE 
        return("School of Computing and Engineering SCE")
    elif (1*int(str1[5])+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10 == (1*2+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10: # If str1 value equal the value those calculated numbers return School of Law
        return("School of Law")
    elif (1*int(str1[5])+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10 == (1*3+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10: # If str1 value equal the value those calculated numbers return College of Arts and Sciences
        return("College of Arts and Sciences")
    else:
        return ("Invalid School") # Return Invalid if above condtions are not met

def get_grade(str2): # Function for below code
     # Asking user for library card string
    if (1*int(str2[6])+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10 == (1*1+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10: # If index 7 value equal the calculated value return Freshmen
        return("Freshman")
    elif (1*int(str2[6])+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10 == (1*2+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10: # If index 7 value equal the calculated value return Sophomore
        return("Sophomore")
    elif (1*int(str2[6])+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10 == (1*3+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10: # If index 7 value equal the calculated value return Junior
        return("Junior")
    elif (1*int(str2[6])+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10 == (1*4+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10: # If index 7 value equal the calculated value return Senior
        return("Senior")
    else: 
        return("Invalid Grade")# Asking user for library card string
    

def character_value(strs):
    return string.ascii_uppercase.index(strs) # returning letter as a integer

def get_check_digit(val):
    return (1*val+2*1+3*2+4*3+5*4+6*1+7*2+8*3+9*4)%10 #Checking digit in the string

def verify_check_digit(value):
    #value = input("Enter a library card: Hit Enter to Exit ==> ")
    #while value != "Exit":
    if len(value) < 10 or len(value) > 10:
        return (False,"The length of the number given must be 10")
    elif value in value[0:5] is not value[0:5].isalpha():
        return (False,"The first 5 characters must be A-Z, the invalid character is at 3 is")
    elif value[-1:-4] != range(0, 10):
        return (False,"The last 3 characters must be 0-9, the invalid character is at 7 is X") 
    elif value[5] != 1 or value[5] != 2 or value[5] != 3:
        return (False,"The sixth character must be 1 2 or 3")
    elif value[6] != 1 or value[6] != 2 or value[6] != 3 or value[6] != 4:
        return (False,"The seventh character must be 1 2 3 or 4")
    else: 
        return(True,"The Card belongs to in", school)
        return(True,"The Card belongs to", grade)
        value = input("Enter a library card: Hit Enter to Exit ==> ")
        


if __name__ == "__main__":
    
    #Main program goes here
    print("Main")
    school = get_school()
    grade = get_grade()
