# while loop continue
# i = 1
# while i<10:
#     print(i)
#     if i==5:
#         break
#     i += 1

# i = 0
# while i<10:
#     i += 1
#     if i==5:
#         continue
#     print(i)
    
# i = 0
# while i<10:
#     i += 1
#     print(i)
# else:
#     print('sakio sakio')

# # sum odd values, even values and all
# no = int(input('Enter a number: '))
# no1, sumEven, sumOdd, sumAll = 0, 0, 0, 0
# while no1 <= no:
#     if no1 % 2 == 0:
#         sumEven += no1
#     else:
#         sumOdd += no1
#     sumAll += no1
#     no1 += 1
# print(f'Sum All is {sumAll}; Sum Odd is {sumOdd}; Sum Even is {sumEven}')

# # Fibonacci sequence
# n = int(input('Enter the count for fibonacci sequence: '))
# count = 0
# n1, n2 = 0, 1
# print(f'Fibonacci up to {n} numbers:')
# while count < n:
#     print(n1)
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3    
#     count += 1
    
# # FOR Loop
# fruits = ['mango', 'litchi', 'apple', 'orange']
# for fruit in fruits:
#     if fruit == 'apple':
#         continue
#     print(fruit)
# else:
#     print('sakio sakio')

# for i in range(1,10,2):
#     print(i)
    
# multiplication table
no = int(input('Enter a number: '))
for i in range(1,11):
    print(f'{no} x {i} = {no*i}')