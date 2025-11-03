import random

# standard list
nList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# search term
sTerm = int(input('Enter a search term: '))

# visit each data element in list, compare sTerm and nList's values to fnd a match
for x in range(0, len(nList)):
    if(sTerm == nList[x]):
        found = True
        print('Found data item', sTerm, 'at position', x)
    else:
        found = False
        print('Not found')
