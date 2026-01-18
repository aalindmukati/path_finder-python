import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#", "#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


def print_maze(maze, stdscr, path): # this def defines the color pair in which the maze will be generated
    blue = curses.color_pair(1)
    red = curses.color_pair(2)

    for i, row in enumerate(maze):  # tells the code to depict that the walls of maze is to be in blue and the path will be red till "X" is found
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", red)
            else:
                 stdscr.addstr(i, j*2, value, blue)

def find_start(maze, start): # code runs to check 0 (which is the starting point)
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i, j)

def find_neighbors(maze, row, col):   # This batch is for code to check for all possible paths to x {Not sure}
    neighbors = []
    if row > 0:
        neighbors.append((row-1, col))
    if row < len(maze)-1:
        neighbors.append((row+1, col))
    if col > 0:
        neighbors.append((row, col-1))
    if col < len(maze[0])-1:
        neighbors.append((row, col+1))
    return neighbors

def find_path(maze, stdscr): # defines the starting position and end position , when start_pos the code runs to check 0 (which is the starting point)
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()      
    q.put((start_pos, [start_pos]))
    visited = {start_pos}

    while not q.empty(): #Checks for the empty space and then visits the col,row
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()
        time.sleep(0.08)

        if maze[row][col] == end:
            return path

        for neighbor in find_neighbors(maze, row, col): # Once the the position is visited , it is check for the shortest path and won't be visited again
            r, c = neighbor
            if neighbor in visited or maze[r][c] == "#":
                continue

            visited.add(neighbor)
            q.put((neighbor, path + [neighbor]))

def main(stdscr):   # Colour of the Maze grid
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main) 

print("Shortest Path Found")