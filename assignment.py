#Kathy Nguyen
#PM
#Guessing Game
import random
#importing the random number generator
random_number = random.randint(1,10)
#random.randint(a,b) to restrict it to only numbers
correct_answer = random_number
previous_guesses = []
#keep it empty to add in numbers later
user_guess = -1
# -1 or any # that is not inside the range to make sure we go straight into the loop


print("Previous Guesses:", previous_guesses)
#this isnt necessary but just so i know theres nothing inside before we start because it was a problem before

while user_guess != random_number:
    user_guess = int(input("Enter a number between 1 and 10: "))
    while user_guess > 10 or user_guess < 1:
        print("Invalid input!, you must enter a number BETWEEN 1 and 10")
        user_guess = int(input("Enter a number between 1 and 10: "))
#while loop above is to make sure its in the range
#immediately have it check coniditions so it can move onto the next loop
    while user_guess in previous_guesses:
        print("Invalid input! Numbers cannot be repeated.")
        user_guess = int(input("Enter a number between 1 and 10: "))
#while loop above is to make sure its NOT a duplicate, will repeat until # is not repeated
#notice how theres no append because we cannot add invalid numbers to the list


    if user_guess > random_number:
        print("Wrong number! The number is LOWER")
    if user_guess < random_number:
        print("Wrong number! The number is HIGHER!")
#regular checks above so we can keep guessing
    previous_guesses.append(user_guess)
#these guesses are valid so we can put them in
#this way the code flows and is minimized properly

    print("Previous Guesses:", previous_guesses)
#again to see your previous guess



print("-----------------------------")
print("Access granted!")
print("Previous answers:", previous_guesses)