# Дано Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# print(grades, 'оценки всех учащихся')
# print(type(grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#print(students)
#print(type(students))
sorted_students = sorted(students)
print(sorted_students)
print(type(sorted_students))
print('_______________')
print(sorted_students[0])




# print(grades[0], 'Aaron оценки')
# print(type(grades[0]))
A = grades[0]
# print(A)
print('_______________')
average_A = sum(A) / len(A)
print(average_A, 'Aaron средний балл')
print('_______________')

# print(type(average_A))

B = grades[1]
print('_______________')
average_B = sum(B) / len(B)
print(average_B, 'Bilbo средний балл')
print('_______________')

J = grades[2]
print('_______________')
average_J = sum(J) / len(J)
print(average_J, 'Johhny средний балл')
print('_______________')

K = grades[3]
print('_______________')
average_K = sum(K) / len(K)
print(average_K, 'Khendrik средний балл')
print('_______________')

S = grades[4]
print('_______________')
average_S = sum(S) / len(S)
print(average_S, 'Steve средний балл')
print('_______________')


#print(A)
#print(B)
#print(J)
#print(K)
#print(S)

print('_______________')

# print(type(a))
# print(a[0])
# print(type(a[0]))



print('_______________')



Average_score = {}
print(Average_score)
Average_score[sorted_students[0]] = average_A
Average_score[sorted_students[1]] = average_B
Average_score[sorted_students[2]] = average_J
Average_score[sorted_students[3]] = average_K
Average_score[sorted_students[4]] = average_S
print(Average_score)
print(type(Average_score))