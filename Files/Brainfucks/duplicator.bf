, Grab a value {x}
[
    >>+ | These two lines move
    <<- | the value to the third cell
    >+  Add the same value to the second cell
    <   Move back to the first
]
So now it looks like this
0  x  x
^

if we want it to to look like
x  x  0
^

Then you have to do this
+ Since the first cell is 0; we have to set it to one for the thing to loop
>>
[
    <<+
    >>-
]
- Then remove it so it isn't x plus 1

Here it is minimized
,[>>+<<->+<]+>>[<<+>>-]-