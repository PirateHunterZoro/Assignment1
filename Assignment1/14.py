"""
To Merge two dictionaries
"""
d = {'x':119,'y':219,'z':319}
c = {'a':122,'b':175,'c':309}

z = d.copy()
z.update(c)

print("Merged Dictionary is {} ".format(z))