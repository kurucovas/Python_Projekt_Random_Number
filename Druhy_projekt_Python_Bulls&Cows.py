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

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

dig_1 = random.choice(digits[1:])
digits.remove(dig_1)  

dig_2 = (random.choice(digits))
digits.remove(dig_2)
    
dig_3 = (random.choice(digits))
digits.remove(dig_3)
    
dig_4 = (random.choice(digits))
    
generated_number = str(dig_1 + dig_2 + dig_3 + dig_4)
#print(generated_number)
    
print("I´ve generated a random 4 digit number for you.\nLet´s play a bulls and cows game.")
print(line)
print("Enter a number:")
print(line)

guess_count = 0
time_start = time.time()

while True:

    entered_number = input(">>>")

    condition1 = (len(entered_number)!= 4)
    condition2 = len(set(entered_number)) != len(entered_number) # set neobsahuje duplicity
    condition3 = entered_number.startswith("0")
    condition4 = entered_number.isdigit()
    if condition1 or condition2 or condition3 or not condition4:
        print("Input is not number: with 4 digits/without duplicated\ndigits/starting without 0/without non-numeric sign")

    entered_set = set(entered_number)
    generated_set = set(generated_number)
    intersection = entered_set & generated_set
    count1 = sum(1 for _ in intersection)
    count2 = sum(1 for i in range(len(entered_number)) if entered_number[i] == generated_number[i]) # Bulls
    count3 = count1 - count2  # Cows
    bulls = "bull" if count2 <= 1 else "bulls"
    cows = "cow" if count3 <= 1 else "cows"
    print(f"{count2} {bulls}, {count3} {cows}")
    print(line)

    guess_count += 1

    if entered_number == generated_number:
        break

time_end = time.time()
total_guess_time = time_end - time_start
print (f"Correct, you´ve guessed the right number\nin {guess_count} guesses in {total_guess_time:.1f} seconds!")
print(line)
print("That´s amazing!")
