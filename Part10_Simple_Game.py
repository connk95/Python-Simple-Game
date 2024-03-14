###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
code = digits[:3]

# Another hint:

def input_check(): 
    guess = input("What is your guess? ")
    
    if guess == None:
        print("Please input a valid three digit number.")
        input_check()
    elif len(guess) != 3:
        print("Please input a valid three digit number.")
        input_check()

    guess_array = [int(i) for i in guess]
    
    score = 0

    for j in code:
        if j == guess_array[0] or j == guess_array[1] or j == guess_array[2]:
            score += 1
    if 1 <= score < 3:
        print("Close: You've guessed a correct number")
        input_check()
    elif score == 0:
        print("Nope: You haven't guess any of the numbers correctly")
        input_check()
    elif score == 3:
        print("Match: You've guessed all numbers correctly")
            
input_check()
            

    
    
        

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

 


