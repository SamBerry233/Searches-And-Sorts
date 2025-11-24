items = [23, 42, 11, 17, 34, 56]
n = len(items)-1 # n is the number of indexes the list has
swapped = True # begins a bubble swap

while(swapped and n>0): # defines whar happens when items arw swapped
    swapped = False # before any items have been swapped, 'swapped' must be false
    for index in range(0, n): # for each item in the list:
        if(items[index] > items[index+1]): # if a swap is possible, meaning it is bigger than the next item in the list:
            temp = items[index] # placeholder storing the index's data
            items[index] = items[index+1] # assign the value of the next item to the currrent item
            items[index+1] = temp # assign the current item's value to the next item

            swapped = True # the items are now swapped

    n = n-1 # one less comparison is needed

print(items) # print the new list now that it has been swapped

