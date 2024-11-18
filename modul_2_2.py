first=input('введите первое целое число: _')
second=input('введите второе целое число: _')
third=input('введите третье целое число: _')
if first == second and second == third:
    print('3')
elif first == second or first == third:
    print('2')
elif first != second and first == third:
    print('2')
elif first != second and second == third:
    print('2')
elif first != second and second != third:
    print('0')