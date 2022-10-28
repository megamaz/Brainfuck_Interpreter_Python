import sys, time, argparse
from pathlib import Path
import datetime

parser = argparse.ArgumentParser(description="Allows for user time limit")
parser.add_argument('-l', '--limit', action='store_true',
                    help='Adds a time limit')
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

def read_and_run_file(IsLimited):
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

    cells = [0]
    tickpos = 0
    run = 0
    try:
        # Grab the file's path
        filename = get_local_path(brainfuckfile + ".bf")

        # operation
        start = datetime.datetime.utcnow()
        with open(filename, 'r') as brainfuck:
            code = split(brainfuck.read())

            remove = len(code)
            while remove > 0:
                if code[remove-1] not in "<>[].,+-":
                    code.remove(code[remove-1])
                
                remove -= 1
            
            if code == []:
                print('File is blank.')
                return

            current = ""
            final_code = []
            for l in code:
                if not l in "><+-":
                    if current != "":
                        final_code.append(current)
                        current = ""
                    final_code.append(l)
                else:
                    if current == "":
                        current += l
                    else:
                        if l != current[-1]:
                            final_code.append(current)
                            current = l
                        else:
                            current += l
            assert ''.join(code) == ''.join(final_code), "code does not match condensed code"
            code:list[str] = final_code

            bracket_indices = {} # not a set: dict
            start_indices = [] # treated as a stack
            for x in range(len(code)):
                if code[x] == "[":
                    start_indices.append(x)
                elif code[x] == "]":
                    val = start_indices.pop(-1)
                    bracket_indices[x] = val
                    bracket_indices[val] = x
            while run < len(code):

                match code[run][0]:
                    case "<":
                        tickpos -= len(code[run])
                        if tickpos < 0:
                            print("Memory error: Cannot go below 0")
                            # print(f"(,{run})")
                            break
                    case ">":
                        tickpos += len(code[run])
                        while tickpos >= len(cells):
                            cells.append(0)
                    
                    # +- runners
                    case "+":
                        cells[tickpos] += len(code[run])
                        cells[tickpos] %= 256
                    case "-":
                        cells[tickpos] -= len(code[run])
                        cells[tickpos] %= 256 # negative modulo 256 will always be [0, 256]
                    
                    # ., runners
                    case ".":
                        print(chr(cells[tickpos]), end="")
                        sys.stdout.flush()
                    case ",":
                        cells[tickpos] = ord(input("> ")[0])
                    
                    # [] runners.
                    case "[":
                        if cells[tickpos] == 0:
                            run = bracket_indices[run]
                    case "]":
                        if cells[tickpos] != 0:
                            run = bracket_indices[run]

                if (datetime.datetime.utcnow() - start).seconds >= 60 and IsLimited:
                    print("\nProgram took too long to run.")
                    return
            
                run += 1

    # if it fails
    except Exception as error:
        print(f'ERROR: {error}')

args = parser.parse_args()
while True:
    
    read_and_run_file(args.limit)
    print("\n---OUTPUT---")

    end = datetime.datetime.utcnow()
    print(f'File ran in {end-start}')