# Работа со словарями:
my_dict={'Сергей' : 1966, 'Дмитрий': 1970, 'Алексей': 1990} # создал переменную и присвоил ей словарь
print(my_dict) # вывел на печать словарь
print(my_dict['Дмитрий'])
my_dict['Антон']=1965 # Если мы 'mnj не напишем = не добавим в словарь
print(my_dict['Антон']) # и тогда результат тут будет с ошибкой
print(my_dict) # вывел на печать словарь
my_dict.update({'Василий': 1999,
                'Ираклий': 2000})
print(my_dict) # вывел на печать словарь
a=my_dict.pop('Антон') # изъяли измножества и сохранили в переменной "А"
print(my_dict) # вывел на печать словарь
print(a) # вывел на печать изъятое "Антон"
# Работа с множествами:
print('-----------------')
my_set={1, 2, 3, 5, 7, 2, 3, (1, 2, 3), 9, 'Слово', 7, 0} # создали множество
print(my_set) # вывел на печать множество
my_set.add(4) # добавили 4ку в множество. могла добавит и так: print(my_set.add(4)) - тогда бы вывилось "none" на печать и добавлась 4ка
my_set.add('Имя')# добавили cтстроку  в множество.
print(my_set)
my_set.discard(2) # удалил элемент"2"
print(my_set)