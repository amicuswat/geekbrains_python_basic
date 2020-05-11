"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом. К
аждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word: str) -> str:
    """
    returns word with first letter capitalized ex: 'text' -> 'Text'
    :param word:
    :return:
    """
    return word.title()


word_lower = input('Введите слово маленькими буквами\n')

print(int_func(word_lower))

words_input = input('Введите несколько слов через пробел, маленькими буквами\n')

words_list = words_input.split(' ')

tmp_list = []
for itm in words_list:
    tmp_list.append(int_func(itm))

new_string = ' '.join(tmp_list)
print(new_string)
