# # ***** Comments
# # # We will start with the variables and different datatypes

# # Python as calculator
# # ''' print(2+2)
# # print(2-3)
# # print(2*3)
# # print(2/3)
# # print(13%2)
# # print(2**3) '''

# # just print
# # print("hellow world")
# # print('hellow world')
# # print("hellow 'w'orld")

# # short cuts with vs code
# # print('hello world1')
# # print('hello world2')
# # print('hello world3')
# # print('hello world4')

# # Datatype - numbers
# # x= 10
# # y = 10.2
# # z = x+y
# # a = 2+3j

# # print(type(x))
# # print(type(y))
# # print(type(z))
# # print(type(a))
# # print(x)

# # Use of library for manipulation of numbers
# # import math
# # print(abs(a))
# # print(math.sqrt(50))
# # print(math.sin(math.radians(30)))
# # # math.

# # ??? Assignment 1-1

# # # String suru bhayo
# # a = 'this is a string'
# # print(a)

# # b = a

# # accessing the characters of string and indexing
# # print(b[:5])
# # print(b[-2:])

# # String concatenation
# # print(a+' ' + b)

# # list
# a = [1,2,3,4,5]
# b = ['a','b','c','d']
# c = ['gapple','danana','cat']
# d = ['apple','dog',1782,1154]

# print(c)

# # change the value of item of list
# c[1] = 'apple'
# print(c)

# # using different modules of list
# a.append(6)

# # ??? assignment 1-2

# Day 2
# a =[1,2,3,4,5]
# b = ['ram', 'hari', 1,2]

# print(len(a))
# print(max(a))
# print(min(a))

# c = [1,2,3,3,3,2,4]
# print(a)

# a.extend(c)
# print(a)

# print(a.count(3))

# a.insert(1,'apple')
# print(a)

# a.remove('apple')
# print(a)

# a_new = a.copy()

# c = a+b

# for binod in a:
#     print(binod)
    
#  tuple sikaum
a = (1,2,3,4,5)
print(a[0])

print(a[-2])
print(type(a))

# a[2] = 5 # wont' run

b = (1,)
print(type(b))

x, y = 1, [2,3,4]
print(type(x))

print(a[0] + a[2])

c =a + b
print(c)

# del c
# print(c)

#  aba set tira lagaum
a = {1,2,3,4,5}
b = {'apple','cat','dog'}

c = {2,3}
print(a.intersection(c))

print(a.union(c,b))

# Assignment 2_1, 2 -> modules of tuple and set (5)

#  la aba dictionary heraum
student = {'name':'Binod', 'age':16, 'addr':'Kaushaltar'}

print(student['name'])

student['age'] = 48

for x in student:
    print(x)

for x in student.values():
    print(x)

print(student.values())

