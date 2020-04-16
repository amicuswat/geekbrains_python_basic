"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

ratings_list = [7, 5, 3, 3, 2]

new_rating = 0

while True:
    new_rating = input("Введите число рейтинга: ")
    if new_rating.isdigit():
        new_rating = int(new_rating)
        break
    else:
        print("Вы ввели не число :(")

i = 1
while i < len(ratings_list):
    print(new_rating, ratings_list[i], ratings_list[i-1])
    if new_rating >= ratings_list[0]:
        ratings_list.insert(0, new_rating)
        break
    elif new_rating <= ratings_list[-1]:
        ratings_list.append(new_rating)
        break
    elif new_rating < ratings_list[i-1] and new_rating >= ratings_list[i]:
        ratings_list.insert(i, new_rating)
        break
    i += 1

print(ratings_list)
