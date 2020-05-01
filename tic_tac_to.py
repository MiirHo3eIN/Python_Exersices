board_list = [" " for x in range(10)]


# To decode the entry
def letter_decoding(letter, pos):
    board_list[pos] = letter


# Layout Structure
def user_gui(board_list):
    print("|-----------|")
    print('| ' + board_list[1] + " | " + board_list[2] + " | " + board_list[3] + " |")
    print("|-----------|")
    print("| " + board_list[4] + " | " + board_list[5] + " | " + board_list[6] + " |")
    print("|-----------|")
    print("| " + board_list[7] + " | " + board_list[8] + " | " + board_list[9] + " |")
    print("|-----------|")


# check entry to be free
def is_space_free(pos):
    return board_list[pos] == " "


# check the board to termnate the game
def is_board_free(board_list):
    if board_list.count(" ") > 1:
        return False
    else:
        return True


# check the winner
def is_winner(board_list, char):
    cond1 = board_list[1] == char and board_list[2] == char and board_list[3] == char
    cond2 = board_list[4] == char and board_list[5] == char and board_list[6] == char
    cond3 = board_list[7] == char and board_list[8] == char and board_list[9] == char
    cond4 = board_list[1] == char and board_list[4] == char and board_list[7] == char
    cond5 = board_list[2] == char and board_list[5] == char and board_list[8] == char
    cond6 = board_list[3] == char and board_list[6] == char and board_list[9] == char
    cond7 = board_list[1] == char and board_list[5] == char and board_list[9] == char
    cond8 = board_list[3] == char and board_list[5] == char and board_list[7] == char
    if (cond1 == True or
            cond2 == True or
            cond3 == True or
            cond4 == True or
            cond5 == True or
            cond6 == True or
            cond7 == True or
            cond8 == True):
        return True
    else:
        return False


# player move:
def player_move():
    run = True
    while run == True:
        try:
            ins = int(input("please insert a digit between 1 to 9: "))
            if ins > 0 and ins < 10:

                if is_space_free(ins):
                    run = False
                    letter_decoding("x", ins)

                else:
                    print("The space is already Taken!")
            else:
                print("please a number between 1 to 9!")
        except:
            print("please insert a number!")


# computer move desciption:
def computer_move():
    possible_moves = []
    for x, letter in enumerate(board_list):
        if letter == " " and x != 0:
            possible_moves.append(x)
    # to determine whether pc will win in the next move.
    move = 0
    for let in ["o", "x"]:
        for i in possible_moves:
            board_cp = board_list[:]  # copy the existed board
            board_cp[i] = let  # check whether this pos leads to win or not
            if is_winner(board_cp, let):
                move = i
                return move
    # if it didn't make through we reach here:
    if 5 in possible_moves:
        move = 5
        return move
    corner_pos = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corner_pos.append(i)
    if len(corner_pos) > 0:
        move = ran_gen(corner_pos)
        return move

    edge_pos = []
    for i in possible_moves:
        if i in [2, 4, 8, 6]:
            edge_pos.append(i)
    if len(edge_pos) > 0:
        move = ran_gen(edge_pos)
        return move
    if possible_moves == []:
        return 0

# random generator:
def ran_gen(li):
    import random
    ln = len(li)
    num = random.randrange(0, ln)
    return li[num]


def tic_toc_logic():
    print("welcome to the Game")
    user_gui(board_list)
    print(is_board_free(board_list))


    while not (is_board_free(board_list)):
        if not (is_winner(board_list, "o")):
            player_move()
            user_gui(board_list)
        else:
            print("You Lost!")
            break
        if not (is_winner(board_list, "x")):
            move = computer_move()
            if move == 0:
                break
            else:
                letter_decoding("o", move)
                print("pc placed o in position " + str(move) + " .")
                user_gui(board_list)
        else:
            print("You Won!")
            break

    if is_board_free(board_list):
        print("Game Ended Tie ")


while True:
    x = input("Do you want to play again? (y/n) ")
    if x.lower() == 'y':
        print('--------------------')
        board_list = [" " for x in range(10)]
        tic_toc_logic()
    elif x.lower() == 'n':
        break