Brayden Roth-White
brayden.roth-white@wsu.edu

RegEx.py takes in a file of postfix expressions in a language Σ=(a,b,c,d,e),
E represents ε and 0 represents the null set, and outputs a table representative
of the associated nfa.

Example of table output
Input: ab+
Output:
q__|____a|____b|____c|____d|____e|______E|
0  |   1 |     |     |     |     |       |
1  |     |     |     |     |     |   5   |
2  |     |   3 |     |     |     |       |
3  |     |     |     |     |     |   5   |
4 S|     |     |     |     |     | 2 , 0 |
5 F|     |     |     |     |     |       |

Start state is labeled with an 'S' and final state is labeled 'F', first column 'q'
is a column for the different states, the numbers in the other columns represent
the state change after the corresponding trigger.

Have file of postfix expressions each on a different line in a plain text file.
Place the plain text file in the same directory as the python files included.
Execute RegEx.py with python launcher and follow the directions that appear on
screen, which should be to enter the file name.

RegEx.py: Main class that makes an nfa and table
Stack.py: Essentially turns append() into push() for aesthetic purposes.
Node.py: Data structure that builds the nfa.

NOTE: Kleene star method uses Thompson's Construction Algorithm rather than
what is described in the project notes.  An nfa is passed in, a new start and
new final state is created, the new start state epsilon jumps to the nfa passed
in and the new final state, the nfa's old final state epsilon jumps to the old
start state of the nfa.  The new nfa is returned.