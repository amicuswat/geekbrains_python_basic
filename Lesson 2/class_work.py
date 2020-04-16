
# var_str = "This is some string of text"
#
#
# # for itm in var_str:
# # for itm in var_str[::-1]:
# for itm in var_str.split(' '):
#      print(itm)

# var_list = [1, 2.3, 'word', True, None]

# var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for itm in var_list[:]: # here a new object it created to iterate
#     var_list.append(itm * 2)
#
# print(var_list)

var_dict = {'key1': 12323,
            'key2': 39027,
            'key3': False,
            }

for key, value in var_dict.items():
    print(f"ключ:{key} -- значение:{value}")
