import random
print("-----------------Guess the Number-----------------")
print("You have 5 chances to guess the number between 1-20.\n")

number = random.randint(1, 30)
# print(number)
nguess = 0

while nguess != 5:
    # print(nguess)
    guess = int(input("Enter your Guess.\n"))
    if guess > 30:
        print("Please Guess a number between 1 to 30.")
    elif guess < number:
        print("Your guess is smaller than the number.")
    elif guess > number:
        print("Your guess is GREATER than the number.")
    elif guess == number:
        print("CONGRATULATIONS! You have Guessed the right number:", number)
    nguess += 1

if nguess == 5:
    print(f"The number was:{number}")
    print("-----------------You lose----------------")

 
