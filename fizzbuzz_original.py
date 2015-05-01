#fizzbuzz.py

newlist = []
for x in range(1,101):

    if x % 5 == 0 and x % 3 == 0:
        newlist.append('fizzbuzz')
    elif x % 3 == 0:
        newlist.append('fizz')
    elif x % 5 == 0:
        newlist.append('buzz')
    else:
        newlist.append(x)
        
print(newlist)