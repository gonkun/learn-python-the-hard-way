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
            if "key" not in inventory:
                monster_room()
            else:
                print("You entered in this room before. Now it seems closed...")
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
        print("You return to the main room.")
        main_room()
    else:
        dead("The faint light disappears for a moment and suddenly you see how lightning strikes you in the chest...")


def monster_room():
    print("You cross the door on the center ...")
    print("There is an unbearable stench along with a grunt.")
    print("You look up and see a huge troll appear from the shadows.")
    print("The door will not open.")
    print("Do you attack or flee across the room? (attack/flee)")

    while True:
        answer = input("> ")

        if answer.lower() == "attack":
            if "sword" not in inventory:
                print("They do not have any weapons.")
                dead("You try to punch the troll in the face. But, as expected, the troll does not flinch and rips your head off.")
            else:
                print("You take out the sword and jump straight to the troll.")
                print("You do a somersault in the air and you put the sword in the neck.")
                print("The monster collapses, and drops a key.")
                print("You have equipped it!")
                inventory.append("key")
                print("You return to the main room.")
                main_room()
        elif answer.lower() == "flee":
            dead("You try to run away, but the troll reaches you makes a soup with your tips")
        else:
            print("Sorry. Can you repeat, please? I don't understand your answer...\n")


def treasure_room():
    print("The room is small but what matters is the center chest.")
    print("The chest is big and old.")
    if "key" not in inventory:
        print("You notice that you do not have the key to open the chest.")
        print("You decide to leave the room and look for it, but the door does not open.")
        dead("You are stuck FOREVER...")
    else:
        print("When you enter the key and observe the wonderful treasure.\n")
        print("Congratulations! You are rich!")
        exit(0)


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
