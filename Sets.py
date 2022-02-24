#Sets

#sets = lists with no duplicate entries

print(set("my name is Eric and Eric is my name".split()))

#only prints {'name', 'and', 'is', 'Eric', 'my'}

#sets have ability to calculate differences and intersections between other sets

#participats in events A and B
a = set(["Sam", "Bailey", "Kayla"])
print(a)
b = set(["Bailey","Jill"])
print(b)

#to determine who attended both, use "intersection"

a = set(["Sam", "Bailey", "Kayla"])
b = set(["Bailey","Jill"])
print(a.intersection(b))
print(b.intersection(a))

#to determine who attended only one of the events, use "symmetric_difference"
a = set(["Sam", "Bailey", "Kayla"])
b = set(["Bailey","Jill"])
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

#to determine who attended only one event and not the other, use "difference"
a = set(["Sam", "Bailey", "Kayla"])
b = set(["Bailey","Jill"])
print(a.difference(b))
print(b.difference(a))

#to determine all participants across both events, use "union"
a = set(["Sam", "Bailey", "Kayla"])
b = set(["Bailey","Jill"])
print(a.union(b))
print(b.union(a))

#print set containing all participants from A who did not attend B
a = set(["Fae", "Rae", "Kay"])
b = set(["Rae", "May"])
print(a.difference(b))