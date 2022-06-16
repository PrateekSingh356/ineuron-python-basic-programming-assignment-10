#4. Write a Python program to find largest number in a list?
l = [3,5,1,6,3]
def find(l):
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    return largest

print("largest element in list is",find(l))