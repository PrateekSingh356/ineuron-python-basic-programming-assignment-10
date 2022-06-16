#6. Write a Python program to find N largest elements from a list?
l = [1,2,34,5,6,78,989,0,3]
def find(l):
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    return largest

print("1st largest element in list is",find(l))
l.remove(989)
print("2nd largest element in list is",find(l))