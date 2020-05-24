import sys
from time import (time,
                  sleep
                  )
import datetime as dt
import json

import itertools
import requests
from my_modules.some_module import my_sum

# print(my_sum(2, 5))

if __name__ == '__main__':
    # print(sys.argv)
    # _, x, y, *z = sys.argv
    # print(z)
    #
    # print(my_sum(int(x), int(y)))
    times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


    def my_cycle(my_iter):
        i = 0
        while True:
            yield my_iter[i]
            i += 1
            if i == len(my_iter):
                i = 0

    for itm in my_cycle(times):
        print(itm)
        sleep(0.5)

#
# for itm in range(10):
#     print(itm)
#     sleep(2)

# def time():
#     return 1
#
#
# print(time())

# response = requests.get('https://geekbrains.ru')
# print(response.text)

# my_dict = {'name': 254365,
#            'surname': 27638638,
#            'lastname': 3920849302,
#            'my_list': [1, 2, 3, 4],
#            'my_tuple': (2, 3, 4, 5),
#            'NONE': None,
#            'BOOL': True,
#            }
#
# j_data = json.dumps(my_dict)
# print(type(my_dict), type(j_data))
# print(j_data)
#
#
# new_data = json.loads(j_data)
# print(type(new_data))
# print(new_data)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# new_list = {itm: itm ** 2 for itm in my_list if not itm & 1}
#
# print(new_list)
