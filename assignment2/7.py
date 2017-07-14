"""
.Write a python script which has class having two below methods and access those methods in another class:

a. getString : get a string from console input
b. printString : to print the string in upper case

"""


class X:
    def getString(self): self.str=input("Enter a string")

    def printString(self): print(self.str)

class Y:
    if __name__ == "__main__":
        x= X()
        x.getString()
        x.printString()


