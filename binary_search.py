def BinarySearch(element, array):
    left = 0
    right = len(array) - 1
    while right - left >= 1:
        middle = (left + right) // 2
        if element > array[middle]:
            left = middle + 1
        else:
            right = middle
    if element != array[right]:    
       return 0
    return right + 1

trash = input()
sorted_sequence = list(map(int, input().split()))
query = list(map(int, input().split()))
for element in query:
    print(BinarySearch(element, sorted_sequence), end = ' ')



