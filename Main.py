# This is a comment, Basic Printing
print('Hello World!')

x = 2
y = 3

print('The answer to 2+3 is ' + str(x+y))

# BODMAS
print('\n')

print((2+3-1)*8/2) # Adding, Subtracting, Multiplying and Dividing
print(11//2)# Answer without Remainder
print(11%2) #Remainder
print(11**2) #Exponents

# Functions
print('\n')

def add(x, y):
  return x + y

print(add(2, 3))

# Statements

print('\n')

if not True:
  print('Not Hello')

elif True:
  print('Hello')

if 9%2 == 0:
  print('Even Number')
else:
  print('Not An Even Number')

# Loops
print('\n')

for i in range(0, 10):
  print(i, end = ' ')
  i += 1

i = 0
while i < 10:
  print(i, end = ' ')
  i += 1

# Data Types
print('\n')

integer = 10
float_or_decimal = 2.9
string = 'Hello'
boolean = True
print(type(boolean))

# Data Structures

print('\n')

unordered_list = [2, 4, 3, 1, 0, 4, 5, 3]
sorted_list = sorted(unordered_list)
print(unordered_list)

# unordered_list.insert(0, 10)
# unordered_list.clear() clears the list
# unordered_list.extend(sorted_list) adds or combines the list with the specified one
# unordered_list.pop(0) removes an element at a given index
# unordered_list.remove(5) removes the occurrence of an elemnt so 5 will be removed
# unordered_list.reverse() reverses the whole list
# unordered_list.count(3) finds the number specified and how many times it is mentioned in the list

number_i_want = 10
found = False

for i in range(len(unordered_list)):
  if unordered_list[i] == number_i_want:
    found = True
    pos = unordered_list.index(unordered_list[i])

if found == True:
  print('The number is found at index ' + str(pos))

elif found == False:
  print('The number does not exist in the list')


print('\n')

strings = 'Hello World'
dictionaries = {
  'Channel Name': 'ssjCoder',
  'About': 'Coding'
}

splitted_string = strings.split('l')
print(splitted_string)

joined_string = 'l'.join(splitted_string)
print(joined_string)

channel_name = dictionaries.get('Channel Name')
print(channel_name)

print('\n')

class HelloWorld():
  print('Hello World')

HelloWorld()

# number_i_want = int(input())
