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

def ins_sort(arr): # insertion sort
    arrLen = len(arr)
    for index in range(1, arrLen):
        item = arr[index]
        position = index - 1
        while position >= 0 and arr[position] > item:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = item
    return arr

start_q = time.perf_counter()
quicksorted_nums = quicksort(numbers.copy())
end_q = time.perf_counter()
print("Quicksorted:", quicksorted_nums)
print(f"Elapsed time (quicksort): {end_q - start_q:.8f} seconds\n")

start_ins = time.perf_counter()
ins_nums = ins_sort(numbers.copy())
end_ins = time.perf_counter()
print("Insertion sorted:", ins_nums)
print(f"Elapsed time (insertion): {end_ins - start_ins:.8f} seconds\n")

start_b = time.perf_counter()
nsub1_bsort_nums = sub_bsort(numbers.copy())
end_b = time.perf_counter()
print("n-1 bubble sorted:", nsub1_bsort_nums)
print(f"Elapsed time (bubble): {end_b - start_b:.8f} seconds")

