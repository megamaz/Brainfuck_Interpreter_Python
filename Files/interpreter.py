import pathlib, sys
from pathlib import Path
import os

def get_local_path(filename):
    return Path(__file__).parents[0] / ('brainfucks//' + filename)

# This is how brainfuck works:
# You have to visualize as if it was just one long row of cells. (30,000 cells) which all start at 0. Each can go up to 255.
# There is a pointer which points at one of the cells. This is the cell that will be edited. To edit the cell, you use the syntaxes.
# Brainfuck only has 8 syntax:
# <     Move the tick one cell to the left
# >     Move the tick one cell to the right
# .     Display the current ASCII value of the cell (E.X; ASCII value 65 = A)
# ,     Accept one character as input and save it's ASCII value (E.X; input B, it will be saved as 66)
# [     Mark the start of a loop. The loop will be ignored if the current value is 0.
# ]     Marks the end of a loop. The loop will be exited if the current cell is 0.
# +     Adds 1 to the current cell.
# -     Removes 1 to the current cell.
# And that's about it. Everything else in brainfuck will be read as comments (or just completely ignored.)

def split(word):
    return [char for char in word]

def ReadAndRunFile():

    print("\n\n------------------\nInsert filename")
    print('''
Leave blank to exit
do not include the .bf\n------------------''')
    brainfuckfile = input("> ")
    if brainfuckfile == "":
        print("thanks for coding in brainfuck lmao")
        sys.exit(0)
    else:
        print("\n"*100)
        
        print("output:", end=' ')

    
    
    cells = [0 for x in range(30000)]
    tickpos = 0
    try:
        # Grab the file's path
        filename = get_local_path(brainfuckfile + ".bf")

        # operation
        run = 0
        skips = 0
        with open(filename, 'r') as brainfuck:
            code = split(brainfuck.read())
            # container = brainfuck.read()
            opening = []
            while run < len(code):

                # <> runners
                if code[run] == "<":
                    if tickpos == 0:
                        print("Memory error: Cannot go to -1")
                        # print(f"(,{run})")
                        break
                    else:
                        tickpos -= 1
                elif code[run] == ">":
                    if tickpos == 30000:
                        print("Memory error: 30000 is limit")
                        # print(f'Character: {code[run]}')
                        # sys.exit(0)
                        break
                    else:
                        tickpos += 1
                
                # +- runners
                if code[run] == '+':
                    if cells[tickpos] == 255:
                        cells[tickpos] = 0
                    else:
                        cells[tickpos] += 1
                elif code[run] == '-':
                    if cells[tickpos] == 0:
                        cells[tickpos] = 255
                        # sys.exit(0)
                    else:
                        cells[tickpos] -= 1
                
                # ., runners
                if code[run] == ".":
                    print(chr(cells[tickpos]), end="")
                    sys.stdout.flush()
                elif code[run] == ",":
                    cells[tickpos] = ord(input("> ")[0])
                

                # [] runners.
                if code[run] == "[":
                    for b in range(len(code)):
                        if b > run:
                            if code[b] == "[":
                                skips += 1
                            
                            if code[b] == "]":
                                if skips == 0:
                                    opening.append((run, b))
                                else:
                                    skips -= 1
                    if cells[tickpos] == 0:
                        for a in opening:
                            if a[0] == run:
                                run = a[1]
                
                if code[run] == "]":
                    if cells[tickpos] != 0:
                        for a in opening:
                            if a[1] == run:
                                run = a[0]
            
                run += 1          

                




    # if it fails
    except Exception as error:
        print("ERROR: ", end='')
        print(error)

while True:
    ReadAndRunFile()