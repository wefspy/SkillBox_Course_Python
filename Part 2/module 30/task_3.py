# Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной. Ссылка на документацию: Documentation.

# Внимательно изучите документацию этого API и напишите программу, которая выводит на экран (и в JSON-файл) 
# информацию о пилотах легендарного корабля Millennium Falcon.

# Информация о корабле должна содержать следующие пункты:
#     название,
#     максимальная скорость,
#     класс,
#     список пилотов.

# Внутри списка о каждом пилоте должна быть следующая информация:
#     имя,
#     рост,
#     вес,
#     родная планета,
#     ссылка на информацию о родной планете.


import requests
import json


url = 'https://swapi.dev/api/starships/'


response = requests.get(url)
ships_data = response.json()


millennium_falcon = next((ship for ship in ships_data['results'] if ship['name'] == 'Millennium Falcon'), None)


pilots_info = []
for pilot_url in millennium_falcon['pilots']:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': pilot_data['homeworld'],
        'homeworld_info': requests.get(pilot_data['homeworld']).json()
    }
    pilots_info.append(pilot_info)


millennium_falcon_info = {
    'название': millennium_falcon['name'],
    'максимальная скорость': millennium_falcon['max_atmosphering_speed'],
    'класс': millennium_falcon['starship_class'],
    'список пилотов': pilots_info
}


print(millennium_falcon_info)


with open('millennium_falcon_info.json', 'w') as file:
    json.dump(millennium_falcon_info, file, indent=4)
    