items = [23, 41, 11, 17, 34, 56]
n = len(items) # defines the number of items in the list
Swaps = 1 # allows the while loop to run
Passes = 0
while Swaps != 0: # if the last pass made any difference, it could be useful to do it again
    Swaps = 0 # the current pass has not done anything yet
    First = 0 # the first index in the list
    Last = First + 1 #the second value to be compared
    Passes += 1
    while Last < n: # if every item was compared
        if items[First] > items[Last]: # if the second item is smaller
            items[First], items[Last] = items[Last], items[First] # move the first item forward
            Swaps += 1 # the items are now swapped
        First += 1 # move onto the next item
        Last = First + 1

print(items) # output

