__author__ = 'Степованый Владислав Геннадьевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Задача-1 :

import random
a=random.randint(0,999999)
i = 0
a = str(a)
while i <= len(a):
    num = int(a[i])
    print(num)
    i = i+1


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# Задача-2 :

a = input("Введите число a")
b = input("Введите число b")
c = a
a = b
b = c
print ("Число а приняло значение = "+a)
print ("Число b приняло значение = "+b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# Задача-3 :

a = int (input("Введите Ваш возраст"))
if a >= 18:
    print ("Доступ разрешен!")
else:
    print ("Извините, пользование данным ресурсом только с 18 лет!")