#8. Write a Python program to print odd numbers in a List?
l = [1,2,3,4,5,667,78,9,0,8,76,5,4,3,2,12]
def findOdd(l):
    for i in l:
        if i%2!=0:
            print(f"{i} is odd number.")
findOdd(l)