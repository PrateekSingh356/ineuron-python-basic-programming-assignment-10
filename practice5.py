#5. Write a Python program to find second largest number in a list?
l = [1,2,34,5,6,78,989,0,3]
def find(l):
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    return largest
l.remove(find(l))
print("2nd largest element in list is",find(l))