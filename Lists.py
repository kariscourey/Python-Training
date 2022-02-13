#Lists

	#Lists
	mylist = []
	mylist.append(1)
	mylist.append(2)
	mylist.append(3)
	print(mylist[0]) #prints 1
	print(mylist[1]) #prints 2
	print(mylist[2]) #prints 3

	#prints out 1,2,3
	for x in mylist:
		print(x)

	mylist = [1,2,3]
	print(mylist[10])

	#Exercise
	numbers = []
	numbers.append(1)
	numbers.append(2)
	numbers.append(3)
	strings = []
	strings.append("hello")
	strings.append("world")
	names = ["John", "Eric", "Jessica"]

	second_name = (names[1])

	#this code should write out the filled arrays and the second name in the list (Eric)
	print(numbers)
	print(strings)
	print("The second name on the list is %s" % second_name)

