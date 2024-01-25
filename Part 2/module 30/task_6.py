# Найдите различия между двумя JSON-файлами. Если различающиеся параметры входят в diff_list, 
# выведите различие. Иными словами, вам нужно отловить изменение определённых параметров и вывести значение: 
# что изменилось и на что. Набор ключей в обоих файлах идентичный, различаются лишь значения.

# Напишите программу, которая: 
#     загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
#     выполняет сравнение параметров, указанных в diff_list;
#     формирует результат в виде словаря;
#     записывает словарь в JSON-файл с названием result.json.

import json


with open('json_old.json', encoding="utf-8") as json_file1:
    json1_dict = json.load(json_file1)


with open('json_new.json', encoding="utf-8") as json_file2:
    json2_dict = json.load(json_file2)


diff_list = ["services", "staff", "datetime"]


result = {}
for key in diff_list:
    if json1_dict['data'][key] != json2_dict['data'][key]:
        result[key] = {
            'old_value': json1_dict['data'][key],
            'new_value': json2_dict['data'][key]
        }

print(result)


with open('result.json', 'w', encoding="utf-8") as outfile:
    json.dump(result, outfile)