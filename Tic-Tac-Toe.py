empty_cells = list("         ")  # empty list consist of 9 empty string used for printing the empty board.
allowable_inputs = []  # empty list will be used for puting all the acceptable inputs coordinates.
# board list is a nested list it represented (x,y) coordinates.
board = [
    [empty_cells[6], empty_cells[3], empty_cells[0]],
    [empty_cells[7], empty_cells[4], empty_cells[1]],
    [empty_cells[8], empty_cells[5], empty_cells[2]]
]
# definding a function for printing the board.
def show_board():
    print("-" * 9)
    print("|",board[0][2], board[1][2], board[2][2], "|")
    print("|",board[0][1], board[1][1], board[2][1], "|")
    print("|",board[0][0], board[1][0], board[2][0], "|")
    print("-" * 9)
show_board()
# loop function for reprecate the inputs till the results appeared (till the loop breaked).
while True:
    def check_coordinates():  # this function for checking if the entered coordinates is allowable or not.
        coordinates = input("Enter the coordinates:").split()
        if coordinates[0].isalpha() or coordinates[1].isalpha():
            print("You should enter numbers!")
        elif int(coordinates[0]) < 1 or int(coordinates[0]) > 3 or int(coordinates[1]) < 1 or int(coordinates[1]) > 3:
            print("Coordinates should be from 1 to 3!")
        elif board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "X" or board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "O":
            print("This cell is occupied! Choose another one!")
        else:
            if len(allowable_inputs) == 0:
                board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "X"
                allowable_inputs.append("X")
            elif allowable_inputs[len(allowable_inputs) - 1] == "X":
                board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "O"
                allowable_inputs.append("O")
            elif allowable_inputs[len(allowable_inputs) - 1] == "O":
                board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "X"
                allowable_inputs.append("X")
            show_board()
    check_coordinates()
    # the below syntax for checking the results (X wins , O wins and Impossible).
    x_wins = ["X", "X", "X"]
    o_wins = ["O", "O", "O"]
    third_row = [board[0][2], board[1][2], board[2][2]]
    second_row = [board[0][1], board[1][1], board[2][1]]
    first_row = [board[0][0], board[1][0], board[2][0]]
    first_col = [board[0][0], board[0][1], board[0][2]]
    second_col = [board[1][0], board[1][1], board[1][2]]
    third_col = [board[2][0], board[2][1], board[2][2]]
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[2][0], board[1][1], board[0][2]]
    winning_matrics = [first_row, second_row, third_row, first_col, second_col, third_col, diagonal_1, diagonal_2]
    count_X = 0
    count_O = 0
    for i in allowable_inputs:
        if i == "X":
            count_X += 1
        if i == "O":
            count_O += 1
    diff_X_O = abs(count_X - count_O)
    if diff_X_O > 1:
        print("Impossible")
        break
    elif x_wins in winning_matrics and o_wins in winning_matrics:
        print("Impossible")
        break
    elif x_wins in winning_matrics:
        print("X wins")
        break
    elif o_wins in winning_matrics:
        print("O wins")
        break
    else:
        if len(allowable_inputs) == 9 and x_wins not in winning_matrics and o_wins not in winning_matrics:
            print("Draw")
            break