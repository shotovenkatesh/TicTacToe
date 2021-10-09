import random

top = ["", "", ""]
middle = ["", "", ""]
bottom = ["", "", ""]
tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
computer_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winning = ["000", "111", "222", "012", "210"]
choice = 1

print("Welcome to Tic Tac Toe!!")
p1 = "x"
p2 = "o"
game_over = False


def show_board():
    print(top)
    print(middle)
    print(bottom)


def placement(player, position):
    if position == 1 and top[0] == "":
        top[0] = player
        return True
    elif position == 2 and top[1] == "":
        top[1] = player
        return True
    elif position == 3 and top[2] == "":
        top[2] = player
        return True
    elif position == 4 and middle[0] == "":
        middle[0] = player
        return True
    elif position == 5 and middle[1] == "":
        middle[1] = player
        return True
    elif position == 6 and middle[2] == "":
        middle[2] = player
        return True
    elif position == 7 and bottom[0] == "":
        bottom[0] = player
        return True
    elif position == 8 and bottom[1] == "":
        bottom[1] = player
        return True
    elif position == 9 and bottom[2] == "":
        bottom[2] = player
        return True
    print("The tile you have chosen has been occupied, please choose a different tile")


def draw_condition():
    if "" not in top and "" not in middle and "" not in bottom:
        return True


def is_win(player):
    if top[0] == player and top[1] == player and top[2] == player:
        return True
    if middle[0] == player and middle[1] == player and middle[2] == player:
        return True
    if bottom[0] == player and bottom[1] == player and bottom[2] == player:
        return True
    for num in winning:
        tile1 = int(num[0])
        tile2 = int(num[1])
        tile3 = int(num[2])
        if top[tile1] == player and middle[tile2] == player and bottom[tile3] == player:
            return True


while not game_over:
    if choice == 1:
        p1_choice = int(input("Player1:  Choose your tile.(1-9): "))
        if p1_choice == 0:
            show_board()
        if p1_choice not in tiles:
            print("Tiles are from 1 to 9.")
        else:
            successfully_placed = placement(p1, p1_choice)
            if successfully_placed:
                choice = 2
                draw = draw_condition()
                winner = is_win(p1)
                if winner:
                    show_board()
                    print("Congratulations Player 1. You are the winner")
                    game_over = True
                elif draw and not winner:
                    show_board()
                    print("This Game is a Draw")
                    game_over = True

    if choice == 2:
        p2_choice = random.choice(tiles)
        computer_tiles.remove(p2_choice)
        successfully_placed = placement(p2, p2_choice)
        if successfully_placed:
            print(f"Computer has chosen tile number {p2_choice}.")
            print("----------------------------------")
            show_board()
            print("----------------------------------")
            choice = 1
            draw = draw_condition()
            winner = is_win(p2)
            if winner:
                show_board()
                print("Computer Wins")
                game_over = True
            elif draw and not winner:
                show_board()
                print("This Game is a Draw")
                game_over = True
