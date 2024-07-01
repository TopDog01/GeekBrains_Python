# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def if_num_is_prime(n):

    for i in range(2, n):
        if n % i == 0:
            return "No"
    return "Yes"
print(if_num_is_prime(7))

def if_num_is_prime2(n, i=2):
    if i < n:
        if n % i == 0:
            return "No"
        return if_num_is_prime2(n, i+1)
    return "Yes"
print(if_num_is_prime2(7))