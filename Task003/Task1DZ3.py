# Знакомство с языком Python (семинары)
# Урок 2. Циклы (for, while)
# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

from random import randint #рандомно задаем число N от 1 до 1 000 000 000
n = randint(1, 1000000000)
print('Ввод - Число N =', n)

i = 0
print('Ответ - Все степени двойки от 1 до N:')
while 2 ** i <= n:
    print(2 ** i, end=" ")
    i += 1