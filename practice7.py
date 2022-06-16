#7. Write a Python program to print even numbers in a list?
l = [1,2,3,4,5,667,78,9,0,8,76,5,4,3,2,12]
def findEven(l):
    for i in l:
        if i%2==0:
            print(f"{i} is even number.")
findEven(l)