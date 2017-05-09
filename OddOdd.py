#Write a function that takes in a list
#and returns the sum of any numbers that occur in odd index, AND
#the value of the number is odd

def OddOdd(values):
	Toggle = True
	SumToReturn = 0
	for value in values:
		if(Toggle==True):
			if(value%2 == 1):
				SumToReturn = SumToReturn+value
		Toggle = not Toggle
	return SumToReturn

print(OddOdd([2,4,6,8,10]))
print(OddOdd([1,3,5,7,9]))
print(OddOdd([2,7,6,13,8]))
print(OddOdd([1,12,3,6,5]))
print(OddOdd([2,4,5,7,8,10,11,13]))
print(OddOdd([1,3,4,6,7,9,10,12]))