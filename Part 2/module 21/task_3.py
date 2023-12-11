# Вы сделали для заказчика структуру сайта по продаже телефонов.
#
# Заказчик рассказал своим коллегам на рынке, и они захотели такой же сайт
# для своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за работу.
#
# Напишите программу, которая запрашивает у клиента количество сайтов, затем названия продуктов,
# а после каждого запроса выводит на экран активные сайты.
#
# Условия:
#       учтите, что функция должна уметь работать с разными сайтами (иначе вам придётся переделывать
# программу под каждого заказчика заново);
#       вы должны получить список, хранящий сайты для разных продуктов
# (а значит, для каждого продукта нужно будет первым делом выполнить глубокое копирование сайта).
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def change_site(obj, prod_name):
    if type(obj) is str:
        return obj.replace('телефон', prod_name).replace('iPhone', prod_name)

    for key in obj:
        obj[key] = change_site(obj[key], prod_name)

    return obj


count_sites = int(input('Сколько сайтов: '))
copies_site = [copy.deepcopy(site) for copying in range(count_sites)]

for num_site in range(count_sites):
    prod_name = input('Введите название продукта для нового сайта: ')
    change_site(copies_site[num_site], prod_name)
    for changed_site in range(num_site + 1):
        print(copies_site[changed_site])