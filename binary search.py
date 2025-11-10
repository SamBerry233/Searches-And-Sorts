# these are the variables this algorithm uses

nlist = [12, 24, 34, 67, 70, 75, 81, 89, 99]
search_term = 75
found = False

"""
'nlist' is the list of items.
'search_term' is the item to be found.
'found' tells us if the item is found, which it isn't because the list hasn't been searched yet.
"""

first = 0
last = len(nlist)-1

# the list ends at the last item, whicb is the 9th item, which occupies the 8th position of the list, so 'last' = '8'.
# 'first' is also '0' because it is the position of the first item.

while(found == False and first <= last):
    mid = (first + last)//2
    if(search_term == nlist[mid]):
        found = true
    elif(search_term > nlist[mid]):
        first = mid + 1
    elif(search_term  < nlist[mid]):
        last = mid - 1

"""
while:
    the item has not been found
    (...and therefore multiple array positions are between the 'first' and 'last' pointers)

then:
    if:
        the item is in the middle position in the list ('mid')
    then:
        the item is found
    whereas, if:
        the item is any distance to the right of the midpoint of the list
    then:
    the list starts after its old midpoint because we know the value is somewhere ahead of said mindpoint
    whereas, if:
    the item is not at the midpoint or to the right
    then:
    it must be to the left, so we'll make the list end before its old midpoint
    
the 'while' loop repeats until the list only contains the item
...
item found
"""

# if(found) means if found == true

if(found):
    print('item found')
else:
    print('item not found')

# end of algorithm
