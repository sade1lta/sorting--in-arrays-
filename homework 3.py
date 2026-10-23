def insertion_sort(array):
    n = len(array)
    i = 1
    while i  < n:
        val = array[i]
        j = i - 1
        while j >= 0 and array[j] > val:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = val 
        i += 1
    return array
arr = [9, 7, 2, 11]
print(insertion_sort(arr))

# 3. worst-case time complexity: 