
# my_list = [1, 2, 3, 4, 5, 0]
# try:
#     a = my_list[10] / 0
# # except ZeroDivisionError:
# #     print("неможно")
# # except IndexError:
# #     print("не хорошо")
# except Exception as ex:
#     print(f"Все ошибки в гости к нам\n{type(ex)} {ex}")
# finally:
#     print("выполнятеся в любом случае")


# def my_test(a: int, b: int) -> int:
#     """
#     Функция складывает а и b и возводит в степень a
#     :param a: int
#     :param b: int
#     :return: int
#     """
#
#     result = (a + b)**a
#
#     return result
#
#
# def test(a: int) -> int:
#     """
#     return int**2
#     :param a: int
#     :return: int
#     """
#     return a**2
#
#
# def my_map(func, tmp):
#     """
#     Applies functions to all elements
#     in iterable and return list of results
#     :param func: func
#     :param tmp: iterable
#     :return: list
#     """
#     result = []
#     for itm in tmp:
#         result.append(func(itm))
#
#     return result
#
#
# def my_map2(func, tmp):
#     for itm in tmp:
#         print("one")
#         yield func(itm)
#         print("two")
#
#
# my_list = [2, 3, 4, 5, 6, 7, 8, 9]
#
# b_list = my_map2(test, my_list)
#
# print(next(b_list))

# for itm in b_list:
#     print(itm)

# a_list = my_map(test, my_list)

# print(b_list)
# print(a_list)

# new_list = list(map(test, my_list))

# new_list = []
# for itm in my_list:
#     new_list.append(itm**2)

# print(new_list)
#
# z = my_test(2, 3)
# print(z)


# def my_sum(a, b, c=22):
#     print('a', a)
#     print('b', b)
#     print('c', c)
#     return a + b + c


# def my_sum(tmp: list):
#     # if not tmp:
#     #     return 0
#     # a = tmp.pop()
#     # a = tmp[0]
#     return tmp[0] + my_sum(tmp[1:]) if tmp else 0


# Named variables
# tmp = my_sum(a=3, c=4, b=8)

# tmp = my_sum(3, 4)

# my_list = [1, 2, 3, 4, 5, 6]

# tmp = my_sum(my_list)

# print(tmp)
# print(my_list)


# def my_sum(*args):
#     print(args)
#     print(type(args))
#     return args[0] + my_sum(*args[1:]) if args else 0
#
#
# tmp = my_sum(1, 2, 3, 4, 5, 6, 7)
#
# print(tmp)


# def my_temp(x, y, z, *args, **kwargs):
#     print(x, y, z)
#     print(args)
#     print(type(kwargs))
#
#     for key, value in kwargs.items():
#         print(f"{key} --- {value}")
#
#
# test = my_temp(1, 2, 3, 4, 5, 'end', hello=22, age=33)

my_list = [1, 2, 3, 4, 5, 6]
a = map(lambda x: x **2, my_list)

b = (lambda x: x ** 2)(213)

print(*a)
print(b)
