"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

WORD_MAX_LENGTH = 10

sentence = input("Введите слова через пробел: \n")

words_list = sentence.split(' ')

for word in words_list:
    if len(word) > WORD_MAX_LENGTH:
        print(word[:10])
    else:
        print(word)
