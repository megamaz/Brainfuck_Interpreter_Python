>[-]<[>>+<+<-]>>[-<<+>>]<<




[-][
NOTE: Any code ran like this: [-][CODE] will not be ran.


This duplicates the value to from the current cell one cell to the right.
Here's how it works;



Let's assume the first cell is set to x.
x  0  0
^

To be completely sure that the value to the right is completely 0 and that the value is duped with no problem, this part is ran: >[-]<
This resets the value on cell to the right to 0. (I like to call it the killer candy, as it looks like candy and "kills" anything from the adjacent cell.)

First things done when entering the loop is to move two cells forward - to the third cell. (x  0 [0])
I add one to the cell, move back one cell and add one to it as well, then go back to x and remove one.
first loop iteration looks like this;
x-1  1   1

since you end on x, as soon as x is zero the grid will look like this.
0  x  x
^

The code for this is this part: [>>+<+<-]



Next thing I do is move the value from the third cell to the starting cell.
x  x  0
      ^

Since the code for this is relatively simple, here is the part that takes care of it: >>[-<<+>>]


When exiting the loop, I move the pointer back to where it was. ("<<" at the end)
The code for this ends up looking like the block at the top. If you want the easier, not minimized version, it is in the area below.
]


[-][

>[-]<               Clear all values from the cell to the right so value can overwrite cell #2
                    If you don't want your value to be overwritten, you can exclude this. do be aware that the outcome will be this instead:
                    x  x+y  0
                    ^

[
    >> +            Move two forward and add one
    < +             Move back and add one there. This is where the magic happens, as the value is added to two cells instead of one.
    < -             Remove one from the firts cell.
]
>>                  Move back to the third cell

[
    -               Remove one from the third cell
    << +            Go back to the first cell and add one, ecentially moving one value from the third cell to the first.
    >>              Go back to the third cell
]<<                 Move back to the first cell where the user can continue with a value duplicated one cell to the right.


]




