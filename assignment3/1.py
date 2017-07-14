""" check if a given key already exists in a dictionary. """

dict={'1':1,'2':2,'3':3}


def keyExists(key):
    return key in dict

if __name__ == "__main__":
    print("Given Key Exists") if keyExists(input("Enter key to check in dict")) else print("Given key doesn't Exist")