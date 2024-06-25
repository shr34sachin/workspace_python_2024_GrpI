#  aaja ko kaksha ma hami conditional statements ko barey ma shikchhyuam
'''
==
>=
<=
!=
if statement
if-else statement
if-elif-else statement
nested if statement
'''
# if condition:
#     statements

a = 45
b = 35
# if b > a:
#     print('b is greater than a')
# elif b == a:
#     print('b is equal to a')
# else:
#     print('a is greater than b')

print('a is greater') if a>b else print('b is greater')

anup = 'a is greater' if a>b else ('b is greater')
print(anup)

binod = 'a greater' if a>b else 'b greater' if b>a else 'equal'
print(binod)

a = int(input('ENter a number:'))
b = int(input('ENter a number:'))
c = int(input('ENter a number:'))

# print('equal') if a==b==c else print('a greater') if a>b>c else print('b greater') if b>a>c else print('c greater') 

# logical operations
if a>b and a>c:
    print('a greater')

#  or
if a>b or a>c:
    print('a is not the smallest number')
    
# not
if not(a<5):
    print('a >=5')

# find largest number
n1, n2, n3 = 10, 22, 15
largest = n1 if n1>n2 and n1>n3 else n2 if n2>n1 and n2>n3 else n3
print(largest)

# print day as per number
no = int(input('Enter a number between 1 to 7: '))
days = ('Sun','Mon','Tues','Wed','Thurs','Fri','Sat')
print('Day is ', days[no-1]) if no<=7 else print('ramrari herne garibaksyos')





