"""
Finds a knight's tour from start position visiting every
board position exactly once.

A knight may make any "L" move which is valid in chess. That is:
any rotation of "up 1 over 2" or "up 2 over 1". The problem
description has a full explanation of valid moves.

Arguments:
    start - (row, col) starting position on board.
    size - number of rows in the square board.
    
Returns:
    List of positions beginning with the start position
    which constitutes a valid tour of the board; visiting
    each position exactly once.
"""
import turtle

def draw_square(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def draw_board(board_size, cell_size):
    turtle.speed(0)  # Fastest speed for drawing board
    colors = ['white', 'black']
    for y in range(board_size):
        for x in range(board_size):
            color = colors[(x + y) % 2]
            draw_square(color, x * cell_size - 200, y * -cell_size + 200, cell_size)

def animate_tour(size, moves):
    cell_size = 50
    board_size = size

    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Knight's Tour")

    # Draw chessboard
    draw_board(board_size, cell_size)

    knight = turtle.Turtle()
    knight.shape("turtle")
    knight.color("blue")
    knight.speed(1)  # Set speed back to slow for the knight's movement
    knight.penup()

    def move_to(x, y):
        knight.goto(x * cell_size - 200 + cell_size // 2, y * -cell_size + 200 - cell_size // 2)
        draw_square("dark blue", x * cell_size - 200, y * -cell_size + 200, cell_size)

    start = moves[0]
    move_to(start[0], start[1])

    for x, y in moves[1:]:
        move_to(x, y)

    turtle.done()




#          -- Move varations and Board creation --
def preparations(start, size):
    board = []
    start = list(start)
    moves = (
        (2, 1), (2, -1), (-2, 1), (-2, -1), 
        (1, 2), (1, -2), (-1, 2), (-1, -2)
            )
    for y in range(size):
        board += [["_" for x in range(size)]]    

    return board, moves, start

#          -- Main calculations --
def calculations(board, moves, start):
    final_moves_list = [start]
    board[start[0]][start[1]] = "K"



    for m1, m2 in moves:
        next_pos = [start[0] + m1, start[1] + m2]
        try:
            if board[next_pos[0]][next_pos[1]] != "K" and 0 <= next_pos[0] < size and 0 <= next_pos[1] < size: 
                return_position = calculations(board, moves, next_pos)
                if return_position:               
                    final_moves_list.extend(return_position)
                    return final_moves_list
                board[next_pos[0]][next_pos[1]] = "_"  
        except IndexError:
            continue
        

    if not any("_" in row for row in board):
        return [start]


def knights_tour(start, size):
    board, moves, start = preparations(start, size)
    return calculations(board, moves, start)




start = (0, 0)
size = 5
moves = knights_tour(start, size)
print(moves)
# animate_tour(size, moves)