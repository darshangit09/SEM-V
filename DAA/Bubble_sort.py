# Python program for implementation of Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # pass i
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # print the array after each pass
        print("Pass", i + 1, ":", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
