#method to compute FIB ( Recursion )
import time
start=time.time()
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
end=time.time()
n = int(input("Enter a number: "))
print(fibonacci(n))
print("Time for Recursion: ")
print(end-start)
