board = [["*", "*", "*"],
         ["*", "*", "*"],
         ["*", "*", "*"]]

has_picked_letter = False

while True:
    pass
    player_1 = input("Pick the letter \"X\" or \"O\"").lower()

    if player_1 == "x":
        player_2 = "o"
        print("If player one is X that means player 2 is O")
        break

    elif player_1 == "o":
        player_2 = "x"
        print("If player one is O that means player 2 is X")
        break

    else:
        print("Pick either X or O")

for i in range(3):
    print(board[i])
