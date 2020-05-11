"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_words = input()

for inx, word in enumerate(user_words.split(' '), 1):
    print(f"{idx}:{word[:10]}")

"""
Мой вариант
"""

# WORD_MAX_LENGTH = 10
#
# sentence = input("Введите слова через пробел: \n")
#
# words_list = sentence.split(' ')
#
# word_num = 1
# for word in words_list:
#     if len(word) > WORD_MAX_LENGTH:
#         print(f"{word_num}:{word[:10]}")
#     else:
#         print(f"{word_num}:{word}")
#     word_num += 1
