"""
Task:
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

LOAD = 1.1

is_correct = False

print("Добрый день, планировщик тренировок готов рассчитать для вас оптимальную нагрузку! \n")
starting_distance = input("Сколько километров вы сейчас пробегаете?: ")
desired_distance = input("Введите целевую дистанцию в км сколько вы хотели бы пробегать?: ")

# костыль
while not is_correct:
    if not starting_distance.isdigit():
        starting_distance = input("Пожалуйта, введите сколько км пробегаете цифрами: ")
        continue
    elif not desired_distance.isdigit():
        desired_distance = input("Пожалуйта, введите ожидаемую дистанцию в км цифрами: ")
        continue
    else:
        is_correct = True

starting_distance = int(starting_distance)
desired_distance = int(desired_distance)

training_days = 1

new_distance = starting_distance

while new_distance < desired_distance:
    print(f"{training_days}-й день тренировки: {new_distance}")
    new_distance = new_distance * LOAD
    training_days += 1

print(f"Ответ: на {training_days}-й день вы достигните результата — не менее {desired_distance} км.")
