"""
Have a hard-coded upper line, n.
Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
Each number should be printed on a new line.
"""

# entering number at command line: working
# entering letter at command line: FINALLY working...
# entering number at raw_input: works, runs process
# entering letter at raw_input: working

import sys

n = ''
        
if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Entered value is not a number...")

while type(n)!=int:
    try:
        n = int(raw_input("Please enter a number: "))
    except ValueError:
        print("Please enter a number...")

print("Fizz buzz counting up to {}".format(n))
for y in range(1,n+1):
    if y % 5 == 0 and y % 3 == 0:
        print('fizzbuzz')
    elif y % 3 == 0:
        print('fizz')
    elif y % 5 == 0:
        print('buzz')
    else:
        print(y)