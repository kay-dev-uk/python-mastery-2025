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

### Python Statements ###

number_3 = 0
if number_3 == 3:
    print('Number 3')
else:
    print('Not 3')

for i in range(7):
    if i == 3:
        print('Number 3')
        
    else:
        print(i)

#Tuple unpacking
my_list = [(1,2), (2,3), (3,4), (4,5)]
for (a,b) in my_list:
    print(a)
    print(b)

my_dict = {'k1': 'v1', 'k2': 'v2', 'k3': 3}
for key,value in my_dict.items():
    print(value)    

#While loops
x = 0
while x < 3:
    print('not 3 yet')
    x += 1

#Operators
word = 'Python'
for letter in enumerate(word):
    print(letter)

# for index, letter in enumerate(word):
# print(index, letter)

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = ['222']

for item in zip(mylist1, mylist2, mylist3):
    print(item)

print('mykey' in {'mykey': 123})

d = {'mykey': 123}
print(123 in d.values())

print(min(mylist1))
print(max(mylist2))

from random import shuffle
shuffle(mylist1)
print(mylist1)

from random import randint
print(randint(0, 4))

result = input('What are you doing? ')
#result is a string
print(result)

#List comprehensions
mystring = 'Americano'
list_1 = [letter for letter in mystring]
print(list_1)

list_2 = [num**2 for num in range(1,101)]
print(list_2)

list_3 = [x for x in range(0,101) if x%2==0]
print(list_3)


### Test ###
#Use for, split() and if to create a statement that will print out words that start with s
st = 'Print only words that start with s in this sentence'
list_st = [word for word in st.split(' ') if word[0].lower() == 's']
for i in list_st:
    print(i)

#Use range() to print all the even numbers from 0 to 10.
print([i for i in range(0,11) if i % 2 == 0])

#Use a List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

print([i for i in range(1,51) if i % 3 == 0])

#Iterate through and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(word + " is even")

#Write a program that prints the integers from 1 to 100. For multiples of 3 print "Fizz" and for multiples of 5 print "Buzz", for both print "FizzBuzz"

for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# Use list comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

print([i[0] for i in st.split(' ')])
