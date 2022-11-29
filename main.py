import random

print('''
   _____                       _______ _              _   _                 _               
  / ____|                     |__   __| |            | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___    |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \   | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/   | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___|   |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                                                                                                     
''')

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)
game_over = False
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    turns = 10
    print("You have 5 attempts remaining to guess the number.")
elif level == "hard":
    turns = 5
    print("You have 10 attempts remaining to guess the number.")
else:
    print("invalid input")


def take_life():
    global turns
    turns -= 1
    return turns


while not game_over:

    guess = int(input("Make a guess: "))
    if guess == answer:
        game_over = True
        print(f"That`s right! The number is {answer}.")
    if guess != answer:
        if guess > answer:
            take_life()
            print(f"This is too high. You have {turns} left")
        elif guess < answer:
            take_life()
            print(f"This is too low. You have {turns} left")
    if turns == 0:
        game_over = True
        print("Out of lives . Game over ..")

