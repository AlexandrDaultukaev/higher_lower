from game_data import data
import random

def getrand(first_number):
    second_number = random.randint(0, 19)
    if second_number == first_number:
        second_number -= 1
    return second_number

def game():
    GAME_OVER = False
    first = getrand(-1)
    second = getrand(first)
    if first == second:
        first -= 1
    while not GAME_OVER:    
        print("Compare A: " + data[first]["name"] + ", a " + data[first]["description"] + ", from " + data[first]["country"] + ".\n")
        print("Against B: " + data[second]["name"] + ", a " + data[second]["description"] + ", from " + data[second]["country"] + ".\n")

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        print("A: " + data[first]["name"] + " has " + str(data[first]["followers"]) + " million followers\n")
        print("B: " + data[second]["name"] + " has " + str(data[second]["followers"]) + " million followers\n")
        if choice == 'A':
            if data[first]["followers"] > data[second]["followers"]:
                first = second
                second = getrand(first)
                print("\n\t\t✔✔✔\n")
            else:
                GAME_OVER = True
                print("\n\t\t✖✖✖\n")
        elif choice == 'B':
            if data[first]["followers"] < data[second]["followers"]:
                first = second
                second = getrand(first)
                print("\n\t\t✔✔✔\n")
            else:
                GAME_OVER = True
                print("\n\t\t✖✖✖\n")
        else:
            print("Don't understand this symbol: " + choice + "\n")
            exit()

game()