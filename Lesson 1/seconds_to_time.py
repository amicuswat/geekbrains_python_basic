"""
Task:
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

seconds = input("Введите количество секунд: ")

# костыль
while not seconds.isdigit():
    seconds = input("Пожалуйта, введите количество секунд цифрами: ")

seconds = int(seconds)

hours = seconds // SECONDS_IN_HOUR
seconds = seconds % SECONDS_IN_HOUR

minutes = seconds // SECONDS_IN_MINUTE
seconds = seconds % SECONDS_IN_MINUTE

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

print(f"{hours}:{minutes}:{seconds}")
