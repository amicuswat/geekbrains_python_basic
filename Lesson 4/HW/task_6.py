"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from time import sleep

from itertools import (count,
                       cycle
                       )

num = 5
some_list = ['Mon', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for itm in count(num):
    print(itm)
    sleep(0.2)
    if itm > 50:
        break

stoper = 0
for itm in cycle(some_list):
    print(itm)
    sleep(0.2)
    stoper += 1
    if stoper > 50:
        break

