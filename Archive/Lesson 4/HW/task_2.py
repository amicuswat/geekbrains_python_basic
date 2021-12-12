"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

from random import randint

my_list = [randint(0, 20) for i in range(10)]
print(my_list)


new_list = []

tmp = my_list[0]
for itm in my_list[1:]:
    if itm > tmp:
        tmp = itm
        new_list.append(itm)

# tmp = my_list[0]
#
# new_list = [itm for itm in my_list[1:] if itm > tmp]

# new_list = [itm for itm in my_list[1:] if my_list[] ]
print(new_list)
