"""
4. Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""


my_list = [1, 2, 3, 4, 2, 4, 5, 1]

new_list = []
# new_list = [itm for itm in my_list if itm not in new_list]

for itm in my_list:
    if itm not in new_list:
        new_list.append(itm)

print(new_list)
