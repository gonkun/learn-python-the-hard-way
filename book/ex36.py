#!/usr/bin/env python

import sys

inventory = []


def dead(text):
    print(text, "You are DIED!")
    exit(0)


def main_room():
    print("You observe the whole room, and you see that there are three door.")
    print("The 3 are identical")

    while True:
        print("what will you open? (left/center/right)")
        choice = input("> ")
        if choice.lower() == "left":
            if "sword" not in inventory:
                mystery_room()
            else:
                print("You entered in this room before. Now it seems closed...")
        elif choice.lower() == "center":
            monster_room()
        elif choice.lower() == "right":
            treasure_room()
        else:
            print("Sorry. Can you repeat, please? I don't understand your answer...")


def mystery_room():
    print("You cross the door on the left ...")
    print("You enter a room slightly lit by the light of the Moon.")
    print("A mural with an inscription that reads as follows stands out in the center of the back wall:\n")
    print("Until I am not measured I am not known. Yet, how do you miss me when I have flown. Who am I?")
    print("It is a riddle. Which is the answer?")
    answer = input("> ")

    if answer.lower() == "the time" or answer.lower() == "time":
        print("The room begins to tremble ... The wall with the inscriptions begins to move until it shows a chest.")
        print("When you open it you discover that inside there is a sword with runes.")
        print("You have equipped it!")
        inventory.append("sword")
        print(inventory)
        print("You return to the main room.")
        main_room()
    else:
        dead("The faint light disappears for a moment and suddenly you see how lightning strikes you in the chest...")


def start():
    print("Hello stranger! You're in front of The Crypt of King Lynch")
    print("Many Great dangers lurk inside. Many have entered to do with the Oracle!")

    while True:
        print("Do you want enter inside? (yes/no)")
        choice = input("> ")
        
        if choice.lower() == "no":
            dead("Oh.. I see... You're another coward. Well, see you soon!")
        elif choice.lower() == "yes":
            print("The dungeon closes after crossing the door...")
            main_room()
        else:
            print("Sorry. Can you repeat, please? I don't understand your answer...\n")

start()
