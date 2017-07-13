"""
Adding elements to list
"""


x=[input("Enter the element") for i in range(int(input("Please enter size of list")))]
print("List created is {}".format(x))


""" you can use a single line to to do this using list comprehensions

x=[input() for i in range(int(input("Please enter size of list")))]

l=[]

You can also follow normal way by appending each element.

for i in range(int(input("Please enter size of list"))):
    l.append(input("Enter the element"))

print("List created is {}".format(l))

"""
