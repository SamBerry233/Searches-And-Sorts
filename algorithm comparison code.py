import time
import random
numbers = [random.randint(1, 100) for x in range(10)]

def sub_bsort(arr): # bubble sort
    n = len(arr)-1
    swapped = True
    while(swapped and n>0):
        swapped = False
        for index in range(0, n):
            if(arr[index] > arr[index+1]):
                temp = arr[index] 
                arr[index] = arr[index+1] 
                arr[index+1] = temp
                swapped = True
        n = n-1
    return(arr)

def quicksort(arr): # quick sort
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    equal = []
    right = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)
    return quicksort(left) + equal + quicksort(right)

def ins_sort(arr):
    arrLen = len(arr)
    for index in range(1, arrLen):
        item = arr[index]
        position = index - 1
        while position >= 0 and arr[position] > item:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = item
    return arr

start_time1 = time.time()
quicksorted_nums = quicksort(numbers)
print("Quicksorted:", quicksorted_nums)
end_time1 = time.time()
elapsed_time1 = end_time1 - start_time1
print(f"Elapsed time: {elapsed_time1:.4f} seconds")

start_time1 = time.time()
ins_nums = ins_sort(numbers)
print("Insertion sorted:", ins_nums)
end_time1 = time.time()
elapsed_time1 = end_time1 - start_time1
print(f"Elapsed time: {elapsed_time1:.4f} seconds")

start_time2 = time.time()
nsub1_bsort_nums = sub_bsort(numbers)
print("n-1 bubble sorted:", nsub1_bsort_nums)
end_time2 = time.time()
elapsed_time2 = end_time2 - start_time2
print(f"Elapsed time: {elapsed_time2:.4f} seconds")
