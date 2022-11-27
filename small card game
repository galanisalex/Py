import random
list1 = ["dragon", "mage", "shaman", "troll", "dwarf", "death knight", "paladin"]
list2 = list1.copy()
hidden = list1 + list2
random.shuffle(hidden)
listcurrent = []
for ele in range(14):
    listcurrent.append(0)
# 0 = closed
# 1 = open
# 2 = temporarily open
print("choose two CLOSED cards (0-13) in order to find a match!")
# Θεωρουμε οτι ο χρηστης ΔΕΝ θα βαλει σε καμια περιπτωση σύμβολο, αλλά μόνον αριθμούς
tries = 0
i = 0
high_score = 0
while True:
# epilogh prwths kartas
    choice1 = float(input("choose first card [0-13]: "))
    while (float(choice1) < 0 or float(choice1) > 13) or listcurrent[int(choice1)] != 0 or choice1 != int(choice1):
        if float(choice1) < 0 or float(choice1) > 13:
            choice1 = float(input("must be an integer between 0 and 13! Try again!: "))
        elif choice1 != int(choice1):
            choice1 = float(input("You must choose an integer! Try again: "))
        else:
            choice1 = float(input("you can't choose a card that's already open! Try again: "))
    listcurrent[int(choice1)] = 2
    print("you opened the card " + str(hidden[int(choice1)]))
# epilogh deyters kartas
    choice2 = float(input("second choice: "))
    while (float(choice2) < 0 or float(choice2) > 13) or listcurrent[int(choice2)] != 0 or choice2 != int(choice2):
        if float(choice2) < 0 or float(choice2) > 13:
            choice2 = float(input("must be an integer between 0 and 13! Try again!: "))
        elif choice2 != int(choice2):
            choice2 = float(input("You must choose an integer! Try again: "))
        else:
            choice2 = float(input("you can't choose a card that's already open! Try again: "))
    print("you opened: " + str(hidden[int(choice2)]))
    if hidden[int(choice1)] == hidden[int(choice2)]:
        print("MATCH FOUND!")
        listcurrent[int(choice1)] = listcurrent[int(choice2)] = 1
    else:
        print("MATCH NOT FOUND")
        listcurrent[int(choice1)] = listcurrent[int(choice2)] = 0
    tries += 1
    if all([v == 1 for v in listcurrent]):
        i += 1
        print("YOU WIN!!!")
        print("number of tries: " + str(tries))
        if i == 1:
            print("That's the new highscore!")
            high_score = tries
        else:
            if high_score > tries:
                print("That's a new high score! your previous highscore was " + str(high_score) + " tries!")
                print("Current high score: " + str(tries) + " tries")
                high_score = tries
        tryagain = str(input("Try again? (Y) for yes, (N) for no: "))
        while tryagain != "Y" and tryagain != "N":
            tryagain = str(input("Invalid input! Type (Y) for yes, or (N) for no: "))
        if tryagain == "Y":
            tries = 0
            for j in range(0, 13+1):
                listcurrent[j] = 0
                random.shuffle(hidden)
        else:
            exit()
