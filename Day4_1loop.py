#  la aba loop wala sikna thalaum
# dui thari ka loop hunxan
# while loop
# for loop

# binod = 10
# while binod > 6:
#     print(' aako aakai')
#     binod -= 1

# val = 0
# days = ('Sun','Mon','Tues','Wed',
#         'Thurs','Fri','Sat')

# while val <= 7:
#     val = int(input('Enter number between 1 to 7, press 8 or more for exit'))
#     print(days[val-1]) if val<=7 else print('we are exiting')
    
val = 'bijay'
days = ('Sun','Mon','Tues','Wed',
        'Thurs','Fri','Sat')
while val != 'exit':
    val = input('Enter 1 to 7, exit fro EXIT: ')
    try:
        val = int(val)
        print(days[val-1]) if val<=7 else print('No between 1 to 7 pls')
    except:
        continue
    
