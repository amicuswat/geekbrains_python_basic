"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def form_input(name, func, var_name):
    """
    get user input, validate it for type, returns var_name and input
    :param name:
    :param func:
    :param var_name:
    :return:
    """
    while True:
        result = input(f"Введите данные о себе \n"
                       f"{name}: ")

        try:
            result = func(result)
            return var_name, result
        except ValueError:
            print(f"Ошибка ввода, попробуйте еще раз")
            continue


def get_user_input(*args):
    """
    Function recieves data cells from template, and forms a dict on user input
    :param args:
    :return:
    """
    result = {}
    print(args)
    for itm in args:
        tmp = form_input(*itm)
        result[tmp[0]] = tmp[1]
    return result


def print_in_line(name='', surname='', year=1900, city='', email='@', phone=''):
    """
    Abundant function, just to practice named vars input
    """
    print(f"Имя - {name}, Фимилия - {surname}, Год рождения - {year}, "
          f"Город проживания - {city}, email - {email}, телефон - {phone}")


user_template = [('Имя', str, 'name'),
                 ('Фамилия', str, 'surname'),
                 ('Год рождения', int, 'year'),
                 ('Город проживания', str, 'city'),
                 ('Email', str, 'email'),
                 ('Телефон', str, 'phone'),
                 ]

user_data = {}

user_data = get_user_input(*user_template)

print_in_line(**user_data)
