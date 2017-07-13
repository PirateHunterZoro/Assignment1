"""
To check if given number is even or odd

returns True if Even, False for Odd
"""

def evenOrOdd(x):
    return int(x)%2==0


if __name__ == "__main__": print("Given No is Even") if evenOrOdd(input()) else print("Given No is Odd")