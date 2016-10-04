# A.Woodward
# October 2016
# Challenge 286 Easy

def reverseFactorial(n):
	term = 2
	value = n
	for i in range(n):
		value = value / term
		if value == 1: return ("%d = %d!" % (n,term))
		term+=1
	return ("%d  NONE"%n)
	
	
	

#Challenge Inputs
print(reverseFactorial(3628800))
print(reverseFactorial(479001600))
print(reverseFactorial(6))
print(reverseFactorial(18))

