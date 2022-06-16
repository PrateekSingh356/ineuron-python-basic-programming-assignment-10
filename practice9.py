#9. Write a Python program to Remove empty List from List?
l = [1,2,3,[24,35,4],[],234,34,23,234,[234,234,34]]
r = []
l = [i for i in l if i != []]
print(l)

