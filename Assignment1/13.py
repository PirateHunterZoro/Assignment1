"""
To check if list is empty or not
"""
def isEmpty(l):
    print("Not an Empty List") if len(l) else print("Empty List")

if __name__ == "__main__":
    l=[]
    isEmpty(l)