from random import randrange
ps = 0
cs = 0
r = 0
h = {}
while True:
    r += 1
    print("Time for Round " + str(r) + "! Current score: Player " + str(ps) + " - PC " + str(cs))
    N = str(input("Choose Rock (R), Paper (P) or Scissors (S): "))
    while N != "R" and N != "P" and N != "S":
        N = str(input("Invalid Input! Rock (R), Paper (P), Scissors (S): "))
    if N == "R":
        print("You choose: Rock")
    if N == "P":
        print("You choose: Paper")
    if N == "S":
        print("You choose: Scissors")
    Options = ["R", "P", "S"]
    PC = Options[randrange(3)]
    if PC == "R":
        print("PC chooses: Rock")
    if PC == "P":
        print("PC chooses: Paper")
    if PC == "S":
        print("PC chooses: Scissors")
    if PC == N:
        print("It's a tie! Nobody wins this round!")
        h[("Round" + str(r))] = {"Player": N, "PC": PC, "Score": (str(ps) + "-" + str(cs))}
    else:
        if PC == "R":
            if N == "P":
                print("Round " + str(r) + ": You win!")
                ps += 1
                h[("Round" + str(r))] = {"Player": N, "PC": PC, "Score": (str(ps) + "-" + str(cs))}
            else:
                print("Round " + str(r) + ": The Computer wins!")
                cs += 1
                h[("Round" + str(r))] = {"Player": N, "PC": PC, "Score": (str(ps) + "-" + str(cs))}
        if PC == "P":
            if N == "R":
                print("Round " + str(r) + ": The Computer wins!")
                cs += 1
                h[("Round" + str(r))] = {"Player": N, "PC": PC, "Score": (str(ps) + "-" + str(cs))}
            else:
                print("Round " + str(r) + ": You win!")
                ps += 1
                h[("Round" + str(r))] = {"Player": N, "PC": PC, "Score": (str(ps) + "-" + str(cs))}
        if PC == "S":
            if N == "P":
                print("Round " + str(r) + ": The Computer wins!")
                cs += 1
                h[("Round" + str(r))] = {"Player": N, "PC": PC, "Score": (str(ps) + "-" + str(cs))}
            else:
                print("Round " + str(r) + ": You win!")
                ps += 1
                h[("Round" + str(r))] = {"Player": N, "PC": PC, "Score": (str(ps) + "-" + str(cs))}
    print('###############################')
    if ps == 3:
        print("You win the match!")
        print("Player " + str(ps) + " - PC " + str(cs))
        break
    if cs == 3:
        print("The Computer wins the match!")
        print("Player " + str(ps) + " - PC " + str(cs))
        break
for key, value in h.items():
    print(str(key) + "->" + str(value))
