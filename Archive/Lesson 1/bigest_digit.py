"""
Task:
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

is_correct = False

number = input("Введите целое положительное число: ")
biggest_digit = 0

# костыль
while not is_correct:
    if not number.isdigit():
        number = input("Пожалуйта, введите число цифрами: ")
        continue
    elif int(number) < 0:
        number = input("Пожалуйта, введите положительное число цифрами: ")
        continue
    else:
        is_correct = True

if len(number) == 1:
    biggest_digit = int(number)
else:
    i = 0
    while i < len(number):
        if biggest_digit > int(number[i]):
            biggest_digit = biggest_digit
        else:
            biggest_digit = int(number[i])

        i = i + 1

print(f"Самая большая цифра: {biggest_digit}")

