def heapify(arr, n, i):
    largest = i
    for child in (2*i+1, 2*i+2):
        if child < n and arr[child] > arr[largest]:
            largest = child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in reversed(range(n//2)):
        heapify(arr, n, i)

    for i in reversed(range(1, n)):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    sample = [12, 11, 13, 5, 6, 7]
    print("Original:", sample)
    heap_sort(sample)
    print("Sorted:", sample)
