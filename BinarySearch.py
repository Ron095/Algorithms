"""
The binary_search function takes a sorted array and an item.
If the item is in the array, the function returns its position.
You'll keep track of what part of the array you have to search through.
"""
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        # The Operator // rounded down, inclusive if the number is 2.9, then is rounded to 2
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return "not exist"


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))

