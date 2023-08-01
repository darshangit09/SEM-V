# method to compute FIB ( itrative )
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)

a=int(input("Enter a number you want Factorial of: "))
fact(a)
