def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # pass i
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # print the array after each pass
        print("After pass", i, ":", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
