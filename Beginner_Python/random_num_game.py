import random
number_to_guess = random.randint(1,10)

guess_count = 1

print("Welcome to the number guess game")

while guess_count <= 4: #They already guessed once

    try:
        guess = int(input('Please guess a number between 1 and 10: '))
    except EOFError as e : pass


    if(guess == number_to_guess): #they guess correctly
        print("Well done you won!")
        print("You took {0} goes to win the game.".format(guess_count))
        break
    elif(guess < number_to_guess):
        print("Your guess was lower than the number")
    else:
        print("Your guess was higher than the number")     
    guess_count += 1
else:
    print("Sorry. You ran out of guesses. The number was {0}.".format(number_to_guess))

print("Game Over")
