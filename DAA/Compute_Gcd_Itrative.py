# method to compute gcd ( itrative )
import time
start=time.time()
def gcd(a, b): 
    while b: 
        a, b = b, a % b 
    return a
end=time.time()
print("The gcd of 60 and 48 is : ")
print(gcd(60, 48))
print("The Time For Itration : ")
print(end-start)
