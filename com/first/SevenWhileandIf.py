secret_number = 1
guess_counter = 0
guess_limit = 3

# check in 1:42 for more : https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=14578s
#condition
while guess_counter < guess_limit:
    guess_counter  +=1
    guess_somenumner = int(input("Guess a number: "))
    if guess_somenumner == secret_number:
        print("You guessed it!")
        break
else:
    print("Sorry, you guessed it wrong.!")

