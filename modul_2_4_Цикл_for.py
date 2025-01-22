numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # Создал список простые числа
not_primes = [] # Список "не простые числа"
for number in numbers:
#    print(number)
    if number == 1:
        continue
    is_prime = True
    for div in range (2, number):
        if number % div == 0:
            not_primes.append(number)
            is_prime = False
            break
        print(f' для числа {number} подбираем делитель {div}')
    if is_prime:
        primes.append(number)
print(numbers)
print(primes)
print(not_primes)