"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys


def salary_calc(work_hours, fee, bonus):
    return work_hours * fee + bonus


if __name__ == '__main__':
    _, hours, fee, bonus, *args = sys.argv

    print(f'Зарплата сотрудника: {salary_calc(int(hours), int(fee), int(bonus))}')