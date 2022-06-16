#3. Write a Python program to find smallest number in a list?
l = [3,5,1,6,3]
def find(l):
    smallest = l[0]
    for i in l:
        if i < smallest:
            smallest = i
    return smallest

print("smallest element in list is",find(l))