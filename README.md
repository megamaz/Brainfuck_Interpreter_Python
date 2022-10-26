# Brainfuck interpreter in Python
Does what it says, inteprets brainfuck using Python.

Be sure to put put the brainfuck files in the `Brainfucks` folder

## How to use
Using it is rather easy. All you really need is to have [Python](https://www.python.org/downloads/) installed. Afterwards, there are **arguments** that can be passed when running the file.
The `run-with-limit.bat` will run the file with a 60sec limit to the code. If you'd rather be able to have an infinite brainfuck code, instead run the `run.bat`.

Occasional updates to this code will come. Instead of downloading, it would be smarter to just pull this every now and then as to not miss any updates. You can run a few of the example files, such as the [HelloWorld.bf](https://github.com/megamaz/Brainfuck_Interpreter_Python/blob/master/Files/Brainfucks/HelloWorld.bf). 


## File Testing

Updates coming to this interpreter are made to improve interpreter speed. [We](https://github.com/coolymike) are currently trying to achieve maximum speed as to make sure that the [mandlebrot.bf](https://github.com/megamaz/Brainfuck_Interpreter_Python/blob/master/Files/Brainfucks/mandlebrot.bf) will run within the 60s time limit. 

Preferably, the entire mandlebrot set would be printed to the console before the 60s are finished. Below are the current outputs.\
Current output (as of Python 3.10.4):
```
AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDEGFFEEEEDDDDDDCCCCCCCCCBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
AAAAAAAAAAAAAAABBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDEEEFGIIGFFEEEDDDDDDDDCCCCCCCCCBBBBBBBBBBBBBBBBBBBBBBBBBB
AAAAAAAAA
```
Current output (as of Python 3.11.0):
```
AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDEGFFEEEEDDDDDDCCCCCCCCCBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
AAAAAAAAAAAAAAABBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDEEEFGIIGFFEEEDDDDDDDDCCCCCCCCCBBBBBBBBBBBBBBBBBBBBBBBBBB
AAAAAAAAAAAAABBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDD
```
