### Day 2 Exercises ###

### Prints the result with float formatting .format() ###
result = 560/223

print("Result is {r:1.2f}".format(r=result))

### F strings ###

print(f'Hey, the result is {result}')

### Lists ###

new_list = [5,145,20,400,2,2.1]
new_list.sort()
new_list.reverse()

print(new_list)

### Dictionaries ###

new_dict = {'k1': 'v1', 'k2': ['v2']}

print(new_dict)


### Tuples ###
new_tuple = (1,2,3,'4')

# Only supports 2 methods: count() and index()

print(new_tuple)

### Sets ###
# Unordered collections of unique elements

new_set = set()
new_set.add(4)
new_set.add(3)
new_set.add(4)
print(new_set)

old_list = [3,3,3,3,2,2,1,3,1,4,5,61,1]
print(set(old_list))

### Test ###
#Write a brief description of the following Object Types and Data Structures
#Numbers: Numerics - Floats or Integers. Ex: 4, 2, 0, -1, 2.3, 333.333
#Strings: Sequence of characters within single or double quotes, strings are immutable. Ex: 'Not a boolean'
#Lists: Orderly and mutable and indexed collection of any data types. Ex: [1,2, 'list']
#Tuples: Ordered and immutable collection of any data types, has only 2 methods. Ex: (1,2,3,'123')
#Dictionaries: Unordered collection of key-value pairs, each key is unique and immutable, values of any data type. Ex: {'3': 'three', '1': 1}

#Write an equation that uses multiplication, division, an exponent, addition and subtraction that is equal to 100.25

print((((40 * 0.5) / 2) ** 2) + 1 - 0.75)

#How to find numbers square root and square?

print(25 ** 0.5)
print(7 ** 2)

#Given the string 'Python'
s = 'Python'
#Reverse
print(s[::-1])

#Two methods to get letter 'o'
print(s[-2])
print(s[4])

#Build a list [1,1,1] in two different ways
ones_list = []
ones_list.append(1)
ones_list.append(1)
ones_list.append(1)
print(ones_list)

ones_list_2 = []
ones_list_2 = [1] * 3
print(ones_list_2)

#Using keys and indexing grab 'Python' from dictionaries:
d = {'k1': {'k2': 'Python'}}
print(d['k1']['k2'])

d = {'k1': [1,2,{'k2': ['another_one', {'easy': [2,3,'Python']}]}]}
print(d['k1'][2]['k2'][1]['easy'][2])

#Use a set to find unique values:
list_to_set = [1,2,3,12,1,1,1,2,3,1,13,13131,22,3,21,3,12]
print(set(list_to_set))

#What's the Boolean output?
l1 = [1,2,[3,4]]
l2 = [1,2,{'k1': 4}]

l1[2][0] >= l2[2]['k1']
#3 >= 4 (=) False
print(l1[2][0] >= l2[2]['k1'])
