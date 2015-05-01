"""
Have a hard-coded upper line, n.
Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
Each number should be printed on a new line.
"""

n = 100
print("Fizz buzz counting up to {}".format(n))
for x in range(1,n+1):
    if x % 5 == 0 and x % 3 == 0:
        #newlist.append('fizzbuzz')
        print('fizzbuzz')
    elif x % 3 == 0:
        #newlist.append('fizz')
        print('fizz')
    elif x % 5 == 0:
        #newlist.append('buzz')
        print('buzz')
    else:
        #newlist.append(x)
        print(x)