#	A.Woodward
#	October 2016
#	Mathagrams
#	Instead of brute force I wanted to try a randomized solution solver
#	Still might add bonuses
#	Challenge #287 Intermediate

import math
import random


def create_list(input):
	
	return_list = []
	num_x = 0
	trim_remain = [1,2,3,4,5,6,7,8,9]
	
	for letter in input:
		if not (letter == " " or letter == "+" or letter == "="):
			return_list.append(letter)
			if(letter == "x"):
				num_x += 1
			else:
				trim_remain.remove(int(letter))
	
	return return_list,num_x, trim_remain
	
	


def list_check(input_list):
	
	first_val = int(input_list[0] + input_list[1] + input_list[2])
	second_val = int(input_list[3] + input_list[4] + input_list[5])
	sum = int(input_list[6] + input_list[7] + input_list[8])
	
	ret_string = str(first_val) + " + " + str(second_val) + " = " + str(sum)
	if first_val + second_val == sum:
		return True, ret_string
	return False, ret_string
	

	


def mathagram_solve(input):
	
	item_list, num_x, remaining = create_list(input)
	
	new_list = item_list[:]
	
	#print("item_list: ", item_list)
	#print("new_list: ", new_list)
	#print("remaining: ", remaining)
	#print("")
	
	for x in range(100000):
		random.shuffle(remaining)
		i = 0
		j = 0
		for item in item_list:
			if item == 'x':
				new_list[i] = str(remaining[j])
				j+=1
			i+=1
		
		#print("item_list: ", item_list)
		#print("new_list: ", new_list)
		#print("remaining: ", remaining)
		#print("")
 		
		bool_check,output_string = list_check(new_list)
 		
		if bool_check:
			return output_string
	
	return "No solution found"
	
	




print(mathagram_solve("1xx + xxx = 468"))
print(mathagram_solve("xxx + x81 = 9x4"))
print(mathagram_solve("xxx + 5x1 = 86x"))
print(mathagram_solve("xxx + 39x = x75"))








