# 11. Write a Python program to Count occurrences of an element in a list?
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
for i in lst:
    print('{} has occurred {} times'.format(i, countX(lst, i)))
