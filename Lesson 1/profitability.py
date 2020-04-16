"""
Task:
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

profit = input("Какова выручка компании: ")
costs = input("Каковы затраты компании: ")

is_correct = False

# костыль
while not is_correct:
    if not profit.isdigit():
        profit = input("Пожалуйта, введите прибыль цифрами: ")
        continue
    elif int(costs) < 0:
        costs = input("Пожалуйта, введите затраты цифрами: ")
        continue
    else:
        is_correct = True

profit = int(profit)
costs = int(costs)

if profit < costs:
    net_loss = costs - profit
    print(f"Внимание! Ваш бизнес убыточен. Вы теряете {net_loss} рублей")
else:
    net_profit = profit - costs
    print(f"Поздравляем! Ваш бизнес прибыльный. Вы зарабатываете {net_profit} рублей")

    number_of_employees = input("Сколько у вас сотрудников: ")

    is_correct = False

    while not is_correct:
        if not number_of_employees.isdigit():
            number_of_employees = input("Пожалуйта, введите количество сотрудников цифрами: ")
            continue
        else:
            is_correct = True

    number_of_employees = int(number_of_employees)

    profit_per_employee = net_profit // number_of_employees

    print(f"Каждый сотрудник в среднем приносит вам {profit_per_employee} рублей")
