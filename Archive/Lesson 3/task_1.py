"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def num_input():

    while True:
        num = input("Введите число: ")

        try:
            num = int(num)
            return num
        except ValueError:
            print("Вы ввели не число")
            continue


def division(a: int, b: int) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        return "На ноль делить нельзя"


first_num = num_input()
second_num = num_input()


result = division(first_num, second_num)

print(result)
