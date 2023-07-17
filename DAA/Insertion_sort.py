import time
start=time.time()
def insertion_sort(arr):
    for i in range(1, len(arr)):
        print("Pass",i)
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        print(arr)
        arr[j + 1] = key
end=time.time()
#arr = input("Enter the elements of the array (space-separated): ").split()
#arr = [int(x) for x in arr]
arr=[1,2,3,3,2,2]
insertion_sort(arr)
print("Average case:", arr)
print(end-start)
print("-------------------------")

arr1=[1,2,3,4,5,6]
insertion_sort(arr1)
print("Best case:", arr1)
print(end-start)
print("-------------------------")

arr2=[9,8,7,6,5,4]
insertion_sort(arr2)
print("Worst case:", arr2)
print(end-start)
print("-------------------------")
