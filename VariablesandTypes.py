#Variables and Types

	#Numbers
	#Do not need to declare variables.
	#Integers(whole numbers) and floating point numbers(decimals)

	myint = 7
	print(myint)

	myfloat = 7.0
	print(myfloat)
	myfloat = float(7)
	print(myfloat)
	myfloat = float(7.1)
	print(myfloat)

	#Strings
	mystring = 'hello'
	print(mystring)
	mystring = "hello"
	print(mystring)

	mystring = "Don't worry about apostrophes"
	print(mystring)
	#mystring = 'Don't worry about apostrophes'

	one = 1
	two = 2
	three = 1 + 2
	print(three)

	hello = "hello"
	world = "world"
	helloworld = hello + " " + world
	print(helloworld)

	a, b = 3, 4
	print(a, b)
	print(a)
	print(b)

	c,d=5,6
	print(c)
	print(d)

	#This will not work!
	one = 1
	two = 2
	hello = "hello"

	print(one + two + hello)

	#Most recent assign of variable will override previous assign

	#Exercise
	mystring = "hello"
	myfloat = 10.0
	myint = 20

	if my string == "hello":
		print("String: %s" % mystring)
	if isinstance(myfloat, float) and myfloat == 10.0:
		print("Float: %f" % myfloat)
	if isinstance(myint, int) and myint == 20:
		print("Integer: %d" % myint)
