import math


def create_list(input):
	
	return_list = []
	num_x = 0
	trim_remain = [1,2,3,4,5,6,7,8,9]
	
	for letter in input:
		if not (letter == " " or letter == "+" or letter == "="):
			print(letter)
			return_list.append(letter)
			if(letter == "x"):
				num_x += 1
			else:
				trim_remain.remove(int(letter))
	
	return return_list,num_x, trim_remain
	
	

def mathagram_solve(input):
	
	item_list, num_x, remaining = create_list(input)
	print(item_list)
	print(num_x)
	print(remaining)
	
	for i in range(factorial(num_x)):
		

	

		









mathagram_solve("1xx + xxx = 468")








