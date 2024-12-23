
# iterative realisation of binary search algorithm
def BinarySearch_iterative(array, target):
    if len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1
    while right - left >= 1:
        middle = (left + right) // 2
        if target > array[middle]:
            left = middle + 1
        else:
            right = middle
    if target != array[right]:
        return -1  # returns -1, if element not in an array
    return left  # returns the position of leftmost occurence of target element


# helping function for BinarySearch_recursive
def BinarySearch_recursive(array, target):
    if len(array) == 0:
        return -1
    return BinarySearch(array, target, 0, len(array) - 1)


# recurcive realisation of binary search algorithm
def BinarySearch(array, target, left, right):
    if right == left:  # exit from recursion
        if target != array[left]:
            return -1  # returns -1, if element not in an array
        else:
            return left  # returns the position of leftmost occurence of target element
    else:  # continuing recursion
        middle = (right + left) // 2
        if target > array[middle]:
            return BinarySearch(array, target, middle + 1, right)
        else:
            return BinarySearch(array, target, left, middle)


if __name__ == "__main__":
    sorted_sequence = list(map(int, input().split()))  # sequence of elements
    query = list(map(int, input().split()))  # sequence of target elements
    for element in query:
        print(
            BinarySearch_iterative(sorted_sequence, element), end=" "
        )  # prints the position of each target element in original sequence
