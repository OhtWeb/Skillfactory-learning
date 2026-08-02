def binary_search(list, target):
    low = list[0]
    high = list[-1]
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == target:
            return True
        if target < guess:
            low = list[0]
            high = mid - 1
            guess = list[mid]
            if guess == target:
                return True
        if target > guess:
            low = mid + 1
            high = list[-1]
            guess = list[mid]
            if guess == target:
                return True
        if target not in list:
            return False
    return None
print(binary_search([1,2,3,4,5,6,7,8,9], 0))