my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list): #
    if my_list[index] > 0:
        print(my_list[index])
        index = index + 1
    elif my_list[index] == 0:
         index = index + 1
         continue
    else:
        break

print(my_list)
print(my_list[2])
print('my_list')
print(f'Наша переменная: {my_list}')