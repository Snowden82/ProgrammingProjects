import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def game_intro():
    print_pause("You find yourself in an open field, you can't stay here.")
    print_pause("It would be a good idea to keep moving.")
    print_pause("People in the community have reported"
                " that there are fierce monsters near here.")
    print_pause("You notice two paths forward.")
    print_pause("One path leads to a dark and dingy cave.")
    print_pause("The other path snakes its way to an abandoned shack.")
    print_pause("In your hand you carry a relatively wimpy pocket knife.\n")


def house(items):
    print_pause("You head toward the shack,"
                " but immediately feel uncomfortable.")

    if "weapon" in items:
        print_pause("You approach the house and chills come across you.")
        print_pause("Suddenly, from nowhere, "
                    "a " + fierce_monster() + " lunges at you!")
        print_pause("Its a good thing that you have"
                    " your " + magical_weapon() + " from the cave!")
        print_pause("You survived the attack and have saved the community!")
        print_pause("You WON! The game is over.\n")
    else:
        print_pause("You approach the house and chills come across you.")
        print_pause("Suddenly, from nowhere, "
                    "a " + fierce_monster() + " lunges at you!")
        print_pause("In this instance, you wonder if it would"
                    " have been better to explore the cave?")
        print_pause("It is far too late to worry about this now")
        print_pause("You plunge your pocket knife"
                    " into the beast, but its not enough.")
        print_pause("You are slain and therefore the game is over.\n")


def cave(items):

    if "weapon" in items:
        print_pause("The cave is practically a dead end now.")
        print_pause("There is nothing else to be found here.")
        print_pause("Have you considered what could "
                    "be found in the abandoned house?\n")
    else:
        print_pause("The cave isn't as dark and dingy as it first appeared")
        print_pause("While you are here, your attention is"
                    " caught by a strange object in the corner of the cave.")
        print_pause("You cant believe it, this weapon is infamous"
                    " and indeed very special.")
        print_pause("You ditch the pocket knife and equip"
                    " yourself with this incredible find.\n")

        items.append("weapon")
    print_pause("You head back to the open field.\n")
    players_choice(items)


def players_choice(items):
    print_pause("Where would you like to go?")

    choice = valid_input("Enter 1 to knock on the door of the house.\n"
                         "Enter 2 to peer into the cave.\n", "1", "2")
    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)


def fierce_monster():
    return random.choice(["Troll", "Sea Monster", "Goblin", "Raving Chicken"])


def magical_weapon():
    return random.choice(["Big Hammer", "Iron Gauntlet",
                          "Mega Mace", "Enchanted Knife"])


def play_again():
    print_pause("Would you like to play again?")

    choice = valid_input("Enter 1 to play again.\n"
                         "Enter 2 to quit.\n", "1", "2")
    if choice == '1':
        print_pause("Fine, do it again, but it does not get any better!")
        play_game()
    elif choice == '2':
        print_pause("Thanks for playing! Make life an adventure!")


def play_game():
    items = []
    game_intro()
    players_choice(items)
    play_again()


play_game()
