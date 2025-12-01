import random
numbers = [random.randint(1, 100) for x in range(10)]
numsLen = len(numbers)

for index in range(1, numsLen):
    item = numbers[index]
    position = index - 1
    while position >= 0 and numbers[position] > item:
        numbers[position + 1] = numbers[position]
        position -= 1

    numbers[position + 1] = item
print(numbers)
