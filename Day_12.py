enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function :{enemies}")


increase_enemies()
print(f"enemies outside function:{enemies}")


#   local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()

#   global scope
player_health = 2


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()

game_level = 3


def create_enemy():
    enemies = ["skeleton", "zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)


#   Modifying Global scope
enemies = 1


def increase():
    print(f"enemies inside function:{enemies}")
    return enemies + 1


increase_enemies()
print(f"enemies outside function:{enemies}")

#   Final project the Guessing game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(guess, answer, turn):
    """check answer against guess.return the number of turn remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    turns = set_difficulty()

    answer = randint(1, 100)
    guess = 0

    while guess != answer:
        print(f"You have{turns} attempts remaining to guess the number")
        guess = int(input("Make a guess!:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have lose")
            return
        elif guess != answer:
            print("Guess again")
    print(f"pssst,the correct answer is {answer}")


game()
