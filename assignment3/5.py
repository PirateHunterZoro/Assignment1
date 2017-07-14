"""
To remove duplicates from list

set removes duplicates.
"""
n=int(input())  # range of list
x=[int(input()) for i in range(n)]
print("Before removing duplicates {}".format(x))
print("After Removing Duplicates {}".format(list(set(x))))
