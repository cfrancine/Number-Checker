number = input("what number?:")
number = int(number)
if number > 0:
	if number % 2 == 0:
		print(+number, "is an even number")
	else:
		print(+number," is an odd number")