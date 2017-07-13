"""
 program to multiplies all the items in a list
"""

from functools import reduce

n=int(input()) # range of list
x=[int(input()) for i in range(n)]

print(reduce(lambda x, y: x*y, x))

