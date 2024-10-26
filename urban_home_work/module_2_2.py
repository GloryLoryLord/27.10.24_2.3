first = int(input('enter first number: '))
second = int(input('enter second number: '))
third = int(input('ender third number: '))

if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
