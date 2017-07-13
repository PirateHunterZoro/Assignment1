"""
To find factorial of given no
"""
def factorial(n):
    if n==0 or n==1: return 1
    else: return n*factorial(n-1)

if __name__ == "__main__":
    n=abs(int(input()))
    print("Factorial of {} is {}".format(n,factorial(n)))