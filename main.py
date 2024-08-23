import random

odd = [1, 3, 5]
even = [2, 4, 6]
verifuser = ["max", "molly", "daisy", "tom"]

Score1 = 0
Score2 = 0

triespass = 0
done = False

turn1 = 0
turn2 = 0

def player1R():
    global Score1, turn1
    P1S = random.randint(1, 6)
    P1S2 = random.randint(1, 6)

    if P1S in odd or P1S2 in odd:
        print("Player 1: You rolled an odd, your numbers were " + str(P1S) + " and " + str(P1S2))
        Score1 -= 5
    if P1S in even or P1S2 in even:
        print("Player 1: You rolled an even, your numbers were " + str(P1S) + " and " + str(P1S2))
        Score1 += 10

    Score1 += P1S + P1S2
    turn1 += 1

def player2R():
    global Score2, turn2
    P2S = random.randint(1, 6)
    P2S2 = random.randint(1, 6)

    if P2S in odd or P2S2 in odd:
        print("Player 2: You rolled an odd, your numbers were " + str(P2S) + " and " + str(P2S2))
        Score2 -= 5
    if P2S in even or P2S2 in even:
        print("Player 2: You rolled an even, your numbers were " + str(P2S) + " and " + str(P2S2))
        Score2 += 10

    Score2 += P2S + P2S2
    turn2 += 1

while not done:
    verif = input("Name to verify user: ").lower()
    if verif in verifuser:
        print("Success")
        while turn1 < 5 and turn2 < 5:
            player1R()
            player2R()
            if turn1 == 5 and turn2 == 5:
                print("Scores")
                print("--------------")
                print("Player 1: " + str(Score1))
                print("Player 2: " + str(Score2))

                if Score1 == Score2:
                    print("It's a tie! Rolling again...")
                    turn1, turn2 = 0, 0  # Reset turns for tiebreaker
                else:
                    if Score1 > Score2:
                        print("Player 1 wins")
                    else:
                        print("Player 2 wins")
                    done = True
    else:
        print("Unsuccessful... Try again")
        triespass += 1
        if triespass == 3:
            print("Locked out")
            done = True
