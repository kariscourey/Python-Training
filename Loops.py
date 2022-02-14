#Loops

#for loop

print("For loops practice.")

primes = [2,3,5,7]

for prime in primes:
    print(prime)

for x in primes:
    print(x)

#for loops can iterate over sequence of numbers using range and xrange
#range = returns new list wih numbers of that specified range
#xrange = returns iterator (more efiicient)
#python 3 uses range function (acts like xrange)

#prints out numbers 0,1,2,3,4
for x in range(5):
    print(x)

#prints 3,4,5
for x in range(3,6):
    print(x)

#prints 3,5,7
for x in range(3,8,2):
    print(x)

#prints 3,6,9
for x in range(3,10,3):
    print(x)

#while loops
#while loops repeat as long as a certain bool condition is met

print("While loops practice.")

#prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1 #this is the same as count = count + 1

#break and continue statements
#break is used to exit a for loop or while loop
#continue used to skip current block and return to the "for" or "while" statement

#prints 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

#prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    #check if x is even
    if x % 2 == 0:
        continue
    print(x)

#prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    #check if x is even
    if x % 2 is 0:
        continue
    print(x)

#else clause for loops ... for - if fail, else is executed ... while - if fail, else is executed
#if break is executed inside for loop, else is skipped
#else is executed even if there's a continue statement

print("Else clause practice.")

#prints 0,1,2,3,4 and then prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count+=1
else:
    print("count value reached %d" %count)

#prints 1,2,3,4
for i in range (1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

#Exercise

print("Exercise practice.")

#prints all even numbers from numbers list in order they are received
#doesn't print any numbers after 237 enters sequence
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]

# your code goes here
for number in numbers:
    if(number == 237):
        break
    else:
        if(number%2 == 0):
            print(number)

# alternative
print("Alternative solution.")

for number in numbers:
    if(number == 237):
        break
    else:
        if(number%2 == 1):
            continue #continues to next iteration ... skip over part of a loop WHEN a condition IS met
    print(number)




