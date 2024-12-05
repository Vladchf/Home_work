numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # Создал список простые числа
not_primes = [] # Список "не простые числа"

for i in range (0, len(numbers)): # i
    is_prime = True
    for j in range (2, numbers[i]):
        if numbers[i] % j == 0 and numbers[i] != 1:
            print(i)
            is_prime = False

    if is_prime and numbers[i] != 1:
        primes.append(numbers[i])
    elif not is_prime and numbers[i] != 1:
       not_primes.append(numbers[i])

print(numbers)
print(primes)
print(not_primes)