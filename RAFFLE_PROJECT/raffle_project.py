# RAFFLE PROJECT

import random as rnd

def main():
    list = []

    print("Press 's' to start the raffle, press 'q' to cancel.")

    while True:                # This loop runs until the user presses either "s" or "q"
        try:
            entry = input("Add Person: ")

            if entry == "q":
                ask = input("Cancel person / Cancel raffle:")
                if ask == "person":
                    ask1 = input("Who do you want to exclude:\n")
                    if ask1 in list:
                        yer = list.index(ask1)
                        list.pop(yer)
                        print("You've excluded this person from the raffle.")
                        print(list)
                    else:
                        print("This person is not in the raffle")
                        print(list)

                elif ask == "raffle":
                    try:
                        while True:
                            list.pop()
                    except:
                        print("The raffle has been cancelled.")

            elif entry == "s":
                ask2 = int(input("How many people will win: "))
                if len(list) < ask2:
                    print("The number of winners cannot exceed the number of participants! \nPlease try again.")
                else:
                    break
            else:
                list.append(entry)

        except:
            print("Incorrect Entry, Please try again!")

    if ask2 > 1:
        winners = rnd.sample(list, ask2)            # This generates a random sample of the participants, with the specified number of winners.
    else:
        winners = [list[0]]             # This creates a list with the first participant, if there is only one winner.

    print("Winners:")
    for winner in winners:
        print(winner)

if __name__ == "__main__":            # It is used in Python to check whether a module is a parent module or not. 
    main()                            # If the module is a main module, the code in the body of the statement is executed.


