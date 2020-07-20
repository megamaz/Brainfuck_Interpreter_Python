import sys, time
from pathlib import Path
import datetime


# This is how brainfuck works:
# You have to visualize as if it was just one long row of cells. (30,000 cells) which all start at 0. Each can go up to 255 (maximum 8-bit value).
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


def get_local_path(filename):
    return Path(__file__).parents[0] / ('brainfucks//' + filename)

def split(word):
    return [char for char in word]

def ReadAndRunFile():
    global start
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
        
        print("---OUTPUT---")

    
        
    
    cells = [0 for x in range(30000)]
    tickpos = 0
    run = 0
    skips = 0
    try:
        # Grab the file's path
        filename = get_local_path(brainfuckfile + ".bf")

        # operation
        
        start = datetime.datetime.utcnow()
        with open(filename, 'r') as brainfuck:
            code = split(brainfuck.read())

            remove = len(code)
            while remove > 0:
                if code[remove-1] == '\n':
                    code.remove(code[remove-1])
                
                remove -= 1
            
            if code == []:
                print('File is blank.')
                return
        

        

        
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
                    for b in range(run+1, len(code)):
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
        print(f'ERROR: {error}')

while True:
    
    ReadAndRunFile()
    print("\n---OUTPUT---")

    end = datetime.datetime.utcnow()
    print(f'File ran in {end-start}')