"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: Simona Kurucova
email: kurucovas11@protonmail.com
"""

import random
import time

print("Hi there!")
line = "-"*50
print(line)

print("I´ve generated a random 4 digit number for you.\nLet´s play a bulls and cows game.")
print(line)
print("Enter a number:")

# Generate secret 4 digit number whereas digits are unique and 1.digit is not zero:
def generate_secret_number():
    first_digit = random.choice(range(1, 10))
    remaining_numbers = random.sample([str(i) for i in range(10) if i != first_digit], 3)
    generated_number = str(first_digit) + ''.join(remaining_numbers)
    return generated_number

# Validation of entered_number:
def validate_number(entered_number):
    condition1 = (len(entered_number) != 4) # entered number is not number with 4 digits
    condition2 = len(set(entered_number)) != len(entered_number) # entered number is not unique
    condition3 = entered_number.startswith("0")  # entered number starts with 0
    condition4 = entered_number.isdigit() # entered number contains only digits
    if condition1 or condition2 or condition3 or not condition4:  # checks if entered number is invalid based on 4 criteria
        print("Input is not a number: with 4 digits/without duplicates\n/starting without 0/without non-numeric sign")
        return False # function returns False when the entered number is invalid
    return True # function returns True when the entered number is valid

# Evaluation of results (bulls and cows):
def evaluate_results(entered_number, generated_number):
    entered_set = set(entered_number)  #conversion of entered numbers into set (set does not contain duplicates)
    generated_set = set(generated_number) #conversion of generated numbers into set
    intersection = entered_set & generated_set # intersection(common digits) between 2 sets 
    # Count of bulls (correct digits and correct position):
    count2 = sum(1 for i in range(len(entered_number)) if entered_number[i] == generated_number[i])   
    # Count of cows (correct digits but incorrect position):
    count1 = sum(1 for _ in intersection) #count number of common digits between entered and generated numbers
    count3 = count1 - count2  # Cows = Intersection count minus Bulls
    bulls = "bull" if count2 <= 1 else "bulls" # distinguish singular/plural (bull/bulls)
    cows = "cow" if count3 <= 1 else "cows"    # distinguish singular/plural (cow/cows)
    print(f"{count2} {bulls}, {count3} {cows}")
    return entered_number == generated_number 

# Main function "play_game" for main game logic
def play_game():
    guess_count = 0
    time_start = time.time()
    generated_number = generate_secret_number() # Generate secret number before loop starts:
    # print(generated_number)
    while True:
        print(line)
        entered_number = input(">>>")
        guess_count += 1
        if not validate_number(entered_number):                  # Validate entered number, if it´s invalid, 
            continue                                             # prompt the user to enter new number
        if evaluate_results(entered_number, generated_number):   # if guess is correct, execute following codes:
            time_end = time.time()
            total_guess_time = time_end - time_start #calculate total time
            print(f"Correct, you´ve guessed the right number\nin {guess_count} guesses in {total_guess_time:.1f} seconds!")
            print(line)
            print("That´s amazing!")
            break   #exit loop because the user has guessed the number
#Run game:
if __name__=="__main__":       
    play_game()