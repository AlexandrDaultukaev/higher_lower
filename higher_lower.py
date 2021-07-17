from game_data import data
import art
import random
import os

clear = lambda: os.system('cls')

def getrand(first_number):
    second_number = random.randint(0, 19)
    while second_number == first_number:
        second_number = random.randint(0, 19)
    return second_number

def print_data(first_person, second_person):
    print("Compare A: " + data[first_person]["name"] + ", a " + data[first_person]["description"] + ", from " + data[first_person]["country"] + ".")
    print(art.vs)
    print("Against B: " + data[second_person]["name"] + ", a " + data[second_person]["description"] + ", from " + data[second_person]["country"] + ".\n")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    print("A: " + data[first_person]["name"] + " has " + str(data[first_person]["followers"]) + " million followers\n")
    print("B: " + data[second_person]["name"] + " has " + str(data[second_person]["followers"]) + " million followers\n")
    return choice

def check_answer(guess, a, b):
    if a > b:
        return guess == "A"
    else:
        return guess == "B"

def game():
    print(art.logo)
    counter = 0
    GAME_OVER = False
    first = getrand(-1)
    second = getrand(first)
    while not GAME_OVER:
        first = second
        second = getrand(first)
        choice = print_data(first, second)
        is_correct = check_answer(choice, data[first]["followers"], data[second]["followers"])
        if is_correct:
            counter += 1
            print("\n\t\t✔✔✔\n\t\tcounter: " + str(counter))
        else:
            GAME_OVER = True
            print("\n\t\t✖✖✖\n\t\tcounter: " + str(counter))

game()