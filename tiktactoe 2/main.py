import random

game_board = [["|_1_|", "|_2_|", "|_3_|"], ["|_4_|", "|_5_|", "|_6_|"], ["|_7_|", "|_8_|", "|_9_|"]]


def check(game_b):
    for point in game_b:
        if point[0] == "|_x_|" or point[0] == "|_o_|":
            if point[0] == point[1] and point[0] == point[2]:
                print(f"PLayer {i[0]} is the winner")
                return True
    if game_b[0][0] == "|_x_|" or game_b[0][0] == "|_o_|":
        if game_b[0][0] == game_b[1][0] and game_b[0][0] == game_b[2][0]:
            print(f"PLayer {game_b[0][0]} is the winner")
            return True
        elif game_b[0][0] == game_b[1][1] and game_b[0][0] == game_b[2][2]:
            print(f"PLayer {game_b[0][0]} is the winner")
            return True
    elif game_b[0][1] == "|_x_|" or game_b[0][1] == "|_o_|":
        if game_b[0][1] == game_b[1][1] and game_b[0][1] == game_b[2][1]:
            print(f"PLayer {game_b[0][1]} is the winner")
            return True
    elif game_b[0][2] == "|_x_|" or game_b[0][2] == "|_o_|":
        if game_b[0][2] == game_b[1][2] and game_b[0][2] == game_b[2][2]:
            print(f"PLayer {game_b[0][2]} is the winner")
            return True
        elif game_b[0][2] == game_b[1][1] and game_b[0][2] == game_b[2][0]:
            print(f"PLayer {game_b[0][0]} is the winner")
            return True


game_on = True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while game_on:
    if len(numbers) == 0:
        game_on = False
    for i in game_board:
        print(i)
    player_x = int(input(f"From {numbers} pick position x"))
    if player_x in numbers:
        numbers.remove(player_x)
        player_o = random.choice(numbers)
        numbers.remove(player_o)
        if player_x == 4 or player_x == 5 or player_x == 6:
            game_board[1][player_x - 4] = "|_x_|"
        elif player_x == 9 or player_x == 7 or player_x == 8:
            game_board[2][player_x - 7] = "|_x_|"
        else:
            game_board[0][player_x - 1] = "|_x_|"
        if player_o == 4 or player_o == 5 or player_o == 6:
            game_board[1][player_o - 4] = "|_o_|"
        elif player_o == 9 or player_o == 7 or player_o == 8:
            game_board[2][player_o - 7] = "|_o_|"
        else:
            game_board[0][player_o - 1] = "|_o_|"
        for i in game_board:
            print(i)
        print("choose again")
    if check(game_board):
        game_on = False

