def selection_sort(array):
    n = len(array)
    for i in range(n - 1): # selecting ith smallest
        smallest = array[i]
        smallest_ind = i
        for j in range(i + 1, n):
            if array[j] < smallest:
                smallest = array[j]
                smallest_ind = j
        # swap if necessary
        if smallest_ind != i:
            (array[i], array[smallest_ind]) = (array[smallest_ind], array[i])

def time_sort(algo, n):
    import time, random

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)

    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

print(time_sort(selection_sort, 32000))