"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def insert_sum(*args):
    result = 0
    exit_flag = False
    try:
        for itm in args:
            result += float(itm) if itm else 0
    except ValueError:
        exit_flag = not exit_flag
    return result, exit_flag


user_sum = 0
while True:
    user_input = input('введите числа через пробел\n').split(' ')
    result_sum, user_exit = insert_sum(*user_input)
    user_sum += result_sum
    print(f"сумму: {user_sum}")

    if user_exit:
        print('Досвиданья')
        break


# total_sum = 0
# is_new_input = True
#
# while is_new_input:
#
#     numbers = input("Введите числа через пробел\n")
#     num_list = numbers.split(' ')
#
#     new_list = []
#     for itm in num_list:
#         try:
#             new_list.append(int(itm))
#         except ValueError:
#             is_new_input = False
#             print(f"Stop at meeting {itm}")
#
#     tmp_sum = sum(new_list)
#     total_sum += tmp_sum
#     print(f"Сумма чисел {tmp_sum} --- общая сумма {total_sum}")
#
# print(total_sum)
