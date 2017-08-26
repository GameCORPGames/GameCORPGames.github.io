print("Welcome to the Funny Sentence Generator by Caleb Sim from Sim Inc.")
leave = input("Press [ENTER] to start or q to leave")
while (leave != "q"):
    adjective1 = input("Give us a adjective: ")
    adjective2 = input("Give us another adjective: ")
    verb1 = input("Give us a verb ending in -ed: ")
    verb2 = input("Give us another verb ending in -ing: ")
    noun1 = input("Give us a noun: ")
    noun2 = input("Give us another noun: \n")
    print("The", adjective1, noun1, verb1, "over the", verb2, adjective2, noun2, ".\n")
    leave = input("Press [ENTER] to continue or q to leave")

