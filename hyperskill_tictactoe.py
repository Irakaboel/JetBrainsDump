game = 0
y = 0
empties = 9
grid_list = ("1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3")
user_input = "_________"
input_list = list(user_input.strip())
# Creating a grid dictionary looking like this: {"1 1": "character1", "1 2": "character2"...} - Makes thinking in rows and columns easier :)
grid = dict(zip(grid_list, input_list))

# Total list of possible combinations
def list_updater():
    global total_list
    total_list = ([grid["1 1"],grid["1 2"],grid["1 3"]], [grid["2 1"],grid["2 2"],grid["2 3"]], [grid["3 1"],grid["3 2"],grid["3 3"]],
                  [grid["1 1"], grid["2 1"], grid["3 1"]], [grid["1 2"], grid["2 2"], grid["3 2"]], [grid["1 3"], grid["2 3"], grid["3 3"]], 
                  [grid["1 1"], grid["2 2"], grid["3 3"]], [grid["1 3"], grid["2 2"], grid["3 1"]])
    return total_list
list_updater()

# Winning conditions
three_X = ["X", "X", "X"]
three_O = ["O", "O", "O"]

# print grid
def printer():
    print("---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------".format(
        grid["1 1"], grid["1 2"], grid["1 3"],
        grid["2 1"], grid["2 2"], grid["2 3"],
        grid["3 1"], grid["3 2"], grid["3 3"]))

def win_con_checker():
    global game
    if three_X in total_list:
        game = 1
    elif three_O in total_list:
        game = 1
    return game

def empty_counter():
    global values
    global empties
    values = "".join(grid.values())
    empties = values.count("_")
    return empties

def tic_tac_toe():
    printer()
    global game
    global y
    global empties
    while game == 0 and empties > 0:
        try:
            # X turn
            x_position = input()
            for i in x_position:
                position_str = "" + i
                number_check = position_str.isdigit()
            if number_check == False:
                    print("You should enter numbers!")
            elif "_" not in grid[x_position] and " " not in grid[x_position]:
                print("This cell is occupied! Choose another one!")
            else:
                grid[x_position] = "X"
                printer()
                # y = "_" in grid.values()
                y += 1
            win_con_checker()
            list_updater()
            empty_counter()
            # O turn
            if game == 0 and empties > 0:
                o_position = input()
                for i in o_position:
                    position_str = "" + i
                    number_check = position_str.isdigit()
                if number_check == False:
                        print("You should enter numbers!")
                elif "_" not in grid[o_position] and " " not in grid[o_position]:
                    print("This cell is occupied! Choose another one!")
                else:
                    grid[o_position] = "O"
                    printer()
                    # y = "_" in grid.values()
                    y += 1
                list_updater()
                empty_counter()
                win_con_checker()
            else:
                game = 1
        except KeyError:
            print("Coordinates should be from 1 to 3!")
    else:
        if three_O in total_list and three_X in total_list:
            print("Impossible")
        elif " " in total_list:
            print("Impossible")
        elif three_X in total_list:
            print("X wins")
        elif three_O in total_list:
            print("O wins")
        elif three_O not in total_list and three_O not in total_list and "_" not in user_input and " " not in user_input:
            print("Draw")
        else:
            print("Draw")
tic_tac_toe()

# game maximum of 9 and breaking as soon as 1 player reaches the goal!