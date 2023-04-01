# Знакомство с языком Python (семинары)
# Урок 2. Циклы (for, while)
# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
n = randint(1, 20)
print('Ввод - Количество монеток на столе:', n)

from random import randint
arraycash = [0] * n
index = 0
while index < n:
    arraycash[index] = randint(0, 1)
    index +=1
print('Ввод - Случайное положение монеток на столе (0 - решкой, 1 -гербом):', arraycash)

countcash0 = 0
countcash1 = 0
for i in arraycash:
    if i == 0:
        countcash0 +=1
    else:
        countcash1 +=1
print('Итого монеток с решкой (0) ->', countcash0)
print('Итого монеток с гербом (1) ->', countcash1)
print('Ответ - Минимальное количество монеток нужно перевернуть ->', min(countcash0, countcash1))