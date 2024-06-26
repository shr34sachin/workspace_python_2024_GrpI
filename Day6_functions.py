# aaja ko kilaas ma hami function sikxaum

# def j(name, duita, teenta):
#     'just trying the function'
#     print(f'hello {name} {duita} {teenta}') #2. ram sam hari
#     name = 'gopal'
#     print(f'hello {name} {duita} {teenta}') #3 gopal sam hari
#     return

# name1 = 'ram'
# name2 = 'sam'
# name3 = 'hari'
# print(f'hello {name1} {name2} {name3}') #1. ram sam hari
# j(name1,name2,name3)
# print(f'hello {name1} {name2} {name3}') #4 ram sam hari

# def passlistfn(list1):
#     print(list1)    # 6 1 2 3
#     list1[2] = 'apple'
#     print(list1)    # 6 1 apple 3
#     return

# list2 = [6, 1, 2, 3]
# print(list2)    # 1. 6 1 2 3
# passlistfn(list2)
# print(list2)    # 6 1 apple 3

# def names(name1, name2='binod'):
#     print(f'{name1} {name2}')

# names('binod','dipika')
# names(name2='dip',name1='ika')

# names('xyz')

# def names(name1, *name2):
#     print(f'{name1} {name2}')

# names('binod','dipika')
# names('xyz','kjdfs','fsdfsa','fsdjaflkjl')

# return values
# def add(n1,n2):
#     return n1 + n2

# x = add(1,2)
# print(x)

# recursion on python
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")

# tri_recursion(6)

# 6 + 5 + 4 + 3 + 2 + 1 + 0 = 21

# lambda function
# sum = lambda a : a * 3
# print(sum(3))

# sum3 = lambda a,b,c: a + b + c
# print(sum3(1,2,3))

def rajeev(n):
    rusha = lambda a: a*n
    return rusha

myDoubler = rajeev(2)
myTripler = rajeev(3)

print(myDoubler(11))
print(myTripler(11))

def swostika(n):
    rusha = lambda a: a**n
    return rusha

pow2 = swostika(2)
pow3 = swostika(3)

print(pow2(3))
print(pow3(3))