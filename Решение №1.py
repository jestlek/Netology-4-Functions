# #Exercise #1
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
# ]

# filtred_geo_logs = []
# for dict_geo_logs in geo_logs:
#     for visit, country in dict_geo_logs.items():
#         if 'Россия' in country:
#             filtred_geo_logs.append(dict_geo_logs)
# print(filtred_geo_logs)

# #Exercise #2
# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}

# set_unique_ids = set()
# for users, ids_ in ids.items():
#     set_unique_ids.update(ids_)
# list_unique_ids = list(set_unique_ids)
# print(list_unique_ids)

# #Exercise #3
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт'
#     ]

# total = len(queries)
# one_word = 0
# two_words = 0
# three_words = 0
# many_words = 0
# for query in queries:
#     query = query.split()
#     if len(query) == 1:
#         one_word += 1
#     elif len(query) == 2:
#         two_words += 1
#     elif len(query) == 3:
#         three_words += 1
#     else:
#         many_words += 1
# one_word_percent = round(one_word / total * 100)
# two_words_percent = round(two_words / total * 100)
# three_words_percent = round(three_words / total * 100)
# many_words_percent = round(many_words / total * 100)
# if one_word > 0:
#     print(f'Поисковых запросов из одного слова - {one_word_percent}%')
# if two_words > 0:
#     print(f'Поисковых запросов из двух слов - {two_words_percent}%')
# if three_words > 0:
#     print(f'Поисковых запросов из трех слов - {three_words_percent}%')
# if many_words > 0:
#     print(f'Поисковых запросов из 4-х и более слов - {many_words_percent}%')
# # Другой вариант решения:
# # storage = {}

# # for query in queries:
# #     words = query.split()

# #     if len(words) in storage.keys():
# #         storage[len(words)] += 1
# #     else:
# #         storage.update({len(words): 1})

# # for key, value in storage.items():
# #     percentage = round((value / len(queries)) * 100, 2)
# #     print(f'Поисковых запросов из {key} слова: {percentage}% ({value} запр.)')

# # Exercise #4
# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# company_max = False
# value_max = False
# for company, value in stats.items():
#     if value > value_max:
#         value_max = value
#         company_max = company
# print(company_max)

# # Exercise #5
# my_list = ['2018-01-01', 'yandex', 'cpc', 100]
# my_dict = my_list[-1]
# for key in my_list[-2::-1]:
#     my_dict = dict({key: my_dict})
# print(my_dict)

month = input('Введите месяц: ')
number = int(input('Введите число: '))
signs = {"март": (21, "Рыбы", "Овен"), "апрель": (21, "Овен", "Телец"), "май": (22, "Телец", "Близнецы"),
        "июнь": (22, "Близнецы", "Рак"), "июль": (23, "Рак", "Лев"), "август": (24, "Лев", "Дева"),
        "сентябрь": (24, "Дева", "Весы"), "октябрь": (24, "Весы", "Скорпион"),
        "ноябрь": (23, "Скорпион", "Стрелец"), "декабрь": (23, "Стрелец", "Козерог"),
        "январь": (21, "Козерог", "Водолей"), "февраль": (20, "Водолей","Рыбы")}
 
 
if (number >= signs[month][0]):
   print(signs[month][2])
else:
   print(signs[month][1])