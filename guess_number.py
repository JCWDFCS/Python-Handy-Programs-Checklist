

import random


limit = 10
def display_title():
    print('Guess the number: ')
    print()

def play_game():
    number = random.randint(1, limit)
    print("I'm thinking of a number from 1 to ", limit)
    count = 1

    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print('Too low.')
            count += 1
        elif guess > number:
            print('Too high.')
            count += 1
        elif guess == number:
            print("You guessed it in " + str(count) + ' tries.\n')
            return

def main():
    display_title()
    again = 'y'
    while again.lower() == 'y':
        play_game()
        again = input("Would you like to play again? (y/n): ")
        print()
    print('Bye!')
#if started with the main module, call the main() function.
if __name__ == "__main__":
    main()
