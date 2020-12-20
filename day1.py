# Time complexity O(n)
def expense_report1(nums_tuple):
	nums_set = set()
	nums_set.update(nums_tuple)
	for num in nums_tuple:
		if (2020-num) in nums_set:
			return num*(2020-num)
	return -1

# Time Complexity O(n^2)
def expense_report2(nums_tuple):
	nums_set = set()
	nums_set.update(nums_tuple)
	for num1 in nums_tuple:
		for num2 in nums_tuple:
			if (2020-num1-num2) in nums_set:
				return (2020-num1-num2)*num1*num2
	return -1

nums_tuple = (1721, 979, 366, 299, 675, 1456)

product1 = expense_report1(nums_tuple)
print(product1)

product2 = expense_report2(nums_tuple)
print(product2)