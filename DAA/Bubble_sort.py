# Python program for implementation of Bubble Sort
import time
start=time.time()
def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				if not swapped:
			              return    
end=time.time()
# Best case
arr1 = [11,12,22,25,34,64, 90]
bubbleSort(arr1)
print("* Best Case *")
print("Sorted array is:")
print(arr1)
print("Time taken by Best Case:", end-start)
print("")

# Average case
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("* Average Case *")
print("Sorted array is:")
print(arr)
print("Time taken by Avg. Case:", end-start)
print("")

#Worst case
arr2 = [11,12,22,25,34,64, 90]
arr2.reverse()
bubbleSort(arr2)
print("* Worst Case *")
print("Sorted array is:")
print(arr2)
print("Time taken by Worst Case:", end-start)
