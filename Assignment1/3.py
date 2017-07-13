"""
To find Prime Number.
"""

def isPrime(x):
    return all([(n % j) for j in range(2, int(n ** 0.5) + 1)]) and n > 1

if __name__ == "__main__":
    n=int(input())
    print("Given No {} is Prime".format(n)) if isPrime(n) else print("Given No {} is Not Prime.".format(n))

