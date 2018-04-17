board = [["*", "*", "*"],
         ["*", "*", "*"],
         ["*", "*", "*"]]


# Make players choose X or O
while True:
    pass
    player_1 = input("Pick the letter \"X\" or \"O\" ").upper()

    if player_1 == "X":
        player_2 = "O"
        print("If player one is X that means player 2 is O")
        break

    elif player_1 == "O":
        player_2 = "X"
        print("If player one is O that means player 2 is X")
        break

    else:
        print("Pick either X or O")

for i in range(3):
    print(board[i])

def good(x):
    if (x < 4):
        return(True)
    else:
        return(False)

player_1_turn = True;
while True:

    # Player 1's turn
    if(player_1_turn):

        player_1_collumn = input("Now choose what collumn your %s is on " % (player_1))
        player_1_row = input("Player 1, choose what row your %s is on " % (player_1))

        if player_1_collumn.isdigit() and player_1_row.isdigit():
            player_1_collumn = int(player_1_collumn) - 1
            player_1_row = int(player_1_row) - 1

            if(good(player_1_collumn) and good(player_1_row)):
                board[player_1_row][player_1_collumn] = player_1

                for i in range(3):
                    print(board[i])

            else:
                print("something's not quite right")
        else:
            print("something's not quite right")
