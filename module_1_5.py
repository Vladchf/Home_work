print ("Неизменяемые и изменяемые объекты. Кортежи и списки")
immutable_var= 1, 2, 'a', 'b', True # записали кортеж
print (immutable_var) # вывели на печать / отобразили
print (type(immutable_var)) # проверил тип списка = кортеж!
print (immutable_var[0])
# immutable_var[0]=200 -   immutable_var[0]=200
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
print ('Создание изменяемых структор данных')
mutable_list = [1, 2, 'Мобильник', True]
print(mutable_list)
print (type(mutable_list))
mutable_list[2]= 'чайник' # меняем элемент с индексом 2 (Мобильник) на чайник
print(mutable_list)