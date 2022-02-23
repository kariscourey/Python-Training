#List Comprehensions

#tool that creates new list based on another list in single, readable line
#e.g. need to create list of integers which specify length of each word in sentence
#but only if the word is not "the"

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split() #splits to array
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)

#using list comprehension, can simplify this process
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

#Exercise
#create new list out of numbers that contains only positive numbers from list as integers
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [round(number) for number in numbers if number > 0]
print(newlist)

#alternatively
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number > 0] #rounds down
print(newlist)