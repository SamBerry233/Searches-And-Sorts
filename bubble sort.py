items = [23, 41, 11, 17, 34, 56]
n = len(items)
Swaps = 1
Passes = 0
while Swaps != 0:
    Swaps = 0
    First = 0
    Last = First + 1
    Passes += 1
    while Last < n:
        if items[First] > items[Last]:
            items[First], items[Last] = items[Last], items[First]
            Swaps += 1
        First += 1
        Last = First + 1

print(items)
