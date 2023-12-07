# При работе с API (application programming interface) сайта биржи по криптовалюте
# вы получили такие данные в виде словаря.
#
# Теперь необходимо обработать эти данные.
#
# Напишите программу, которая выполняет следующий алгоритм действий:
#     Вывести списки ключей и значений словаря.
#     В ETH добавить ключ total_diff со значением 100.
#     Внутри fst_token_info значение ключа name поменять с fdf на doge.
#     Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
#     Внутри sec_token_info изменить название ключа price на total_price.
#
# После выполнения алгоритма выводить результат (словарь) не нужно.

data = \
{
    "address": "0x544444444444",
    "ETH":
    {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens":
    [
        {

            "fst_token_info":
            {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info":
            {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

#  ---{ Пункт 1 }---
def get_keys_value_dict_and_subDict(obj):
    if type(obj) == dict:
        print(obj.keys())
        print(obj.values())
        print()
        for value in obj.values():
            get_keys_value_dict_and_subDict(value)

    elif type(obj) == tuple or type(obj) == list:
        for item in obj:
            get_keys_value_dict_and_subDict(item)

    return

get_keys_value_dict_and_subDict(data)

#  ---{ Пункт 2 }---
data['ETH']['total_diff'] = 100
print()

#  ---{ Пункт 3 }---
data['tokens'][0]['fst_token_info']['name'] = 'doge'

#  ---{ Пункт 4 }---
data['ETH']['totalOut'] += (data['tokens'][0].pop('total_out')
                            + data['tokens'][1].pop('total_out'))

#  ---{ Пункт 5 }---
value_old_key = data['tokens'][1]['sec_token_info'].pop('price')
data['tokens'][1]['sec_token_info']['total_price'] = value_old_key

