import copy
import os

NUM_ROWS = 3
NUM_COLS = 3
EMPTY_SYMBOL = " "

def get_empty_grid(num_cols, num_rows, empty_symbol):
    grid = []

    for x in range(num_rows):
        row = []
        for _ in range(num_cols):
            row.append(empty_symbol)
        grid.append(row)
    return grid

def print_grid(grid):
    for i in range(NUM_ROWS):
        print(grid[i])

def check_scores(player, grid, points):
    print()
    return score_result

def player_input(player_indication, grid):
    os.system('cls' if os.name == 'nt' else 'clear')

    print_grid(grid)
    print()

    print('Where add ', player_indication,' symbol?')
    x_axis = int(input('In X axis (0..2): '))
    y_axis = int(input('In Y axis (0..2): '))


    grid[y_axis][x_axis] = player_indication

    return grid

# ------------------------------------MAIN-----------------------------------------

points = [
        [[0, 0], [0, 1], [0, 2]], # 1 horizontal line
        [[1, 0], [1, 1], [1, 2]], # 2 horizontal line
        [[2, 0], [2, 1], [2, 2]], # 3 horizontal line
        [[0, 0], [1, 0], [2, 0]], # 1 vertical line
        [[0, 1], [1, 1], [2, 1]], # 2 vertical line
        [[0, 2], [1, 2], [2, 2]],  # 3 vertical line
        [[2, 2], [1, 1], [0, 0]], # \ cross line
        [[2, 0], [1, 1], [0, 2]]  # / cross line
        ]

def main():
    game_over = False
    grid = get_empty_grid(NUM_COLS, NUM_ROWS, EMPTY_SYMBOL)

    while not game_over:

        print(player_input('X', grid))
        print(player_input('O', grid))

        # os.system('cls' if os.name == 'nt' else 'clear')

        # print_grid(grid)
        # print()

        # print('First player: Where add "X" symbol?')
        # x_value_x_axis = int(input('In X axis (0..2): '))
        # x_value_y_axis = int(input('In Y axis (0..2): '))

        # grid[x_value_y_axis][x_value_x_axis] = 'X'

        # os.system('cls' if os.name == 'nt' else 'clear')

        # print_grid(grid)
        # print()

        # print('Second player: Where add "O" symbol?')
        # o_value_x_axis = int(input('In X axis (0..2): '))
        # o_value_y_axis = int(input('In Y axis (0..2): '))

        # grid[o_value_y_axis][o_value_x_axis] = 'O'

        os.system('cls' if os.name == 'nt' else 'clear')

        print_grid(grid)

        lines_counter = []
        x_list = []

        for z in range(len(points)):
            for c in range(len(points[z])):
                lines_counter.append(grid[points[z][c][0]][points[z][c][1]])

            x_counter = lines_counter.count("X")
            x_list.append(x_counter)
            lines_counter = []
        print(x_list)

        if 3 in x_list:
            print('Winner is X palyer')
            game_over = True

        print()
        input("Press ENTER")

if __name__ == '__main__':
    main()