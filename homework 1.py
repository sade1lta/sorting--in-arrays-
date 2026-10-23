# 2. 
def selection_sort(array):
    n = len(array)
    for i in range(n - 1): 
        smallest = array[i]
        smallest_ind = i
        for j in range(i + 1, n):
            if array[j] < smallest:
                smallest = array[j]
                smallest_ind = j
        # swap if necessary
        if smallest_ind != i:
            print(array)
            (array[i], array[smallest_ind]) = (array[smallest_ind], array[i])

def bubble_sort(array):
    n = len(array)
    ordered = False
    while not ordered:
        print(array)
        ordered = True
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                (array[i], array[i + 1]) = (array[i + 1], array[i])
                print(array)
                ordered = False

arr1 = [-4, 11, 7, -12, 6, 1]
arr2 = [-4, 11, 7, -12, 6, 1]
selection_sort(arr1)
print(arr1)
bubble_sort(arr2)
print(arr2)
