# Exercise #4
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
# stats_sort = sorted(stats.items(), key=lambda x:x[1], reverse=True)
# print(stats_sort[0][0])
print(max(stats, key=stats.get))

# Exercise #1
# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
#     ]
# filtred_geo_logs = dict()
# for visits in geo_logs:
#     if 'Россия' in list(*visits.values()):
#         filtred_geo_logs.update(visits)
# print([filtred_geo_logs])

# #Exercise #2
# # ids = {'user1': [213, 213, 213, 15, 213],
# #        'user2': [54, 54, 119, 119, 119],
# #        'user3': [213, 98, 98, 35]}
# # set_ids = set()
# # for ids_ in ids.values():
# #     set_ids.update(ids_)
# # print(list(set_ids))

# Exercise #3
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт'
#     ]

# my_dict = {}
# for query in queries:
#     words = query.split()
#     if len(words) in my_dict:
#         my_dict[len(words)] += 1
#     else:
#         my_dict.update({len(words): 1})

# for key, value in my_dict.items():
#     percent = round(value / len(queries) * 100, 2)
#     print(f'Ключевых фраз из {key} слов - {percent}%, количество запросов = {value}')

# # Другое решение:
# total_request_quantity = len(queries)  # общее кол-во запросов

# dct = {}  # Временный словарь куда пишем статистику своеобразная база данных

# for query in queries:
#     count = len(query.split())
#     dct[count] = dct.get(count, 0) + 1

# # Для каждого элемента словаря, т.е. для каждого кол-ва слов расчитываем процент и выводим на печать
# for key in dct:
#     percent_of_queries = round(dct[key] / total_request_quantity * 100)
#     print(f'Кол-во слов в запросе {key}  - {percent_of_queries}')

# # # Exercise #5
# my_list = ['2018-01-01', 'yandex', 'cpc', 100]
# my_dict = my_list[-1]
# for i in my_list[-2::-1]:
#     my_dict = {i:my_dict}
# print(my_dict)