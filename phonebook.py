from random import *
import json

sp = {'Игорь Сергеев': {'Номер телефона' : ['8952529299', '8955542335'], 'Место жительства': 'Рязань', 'Кем приходится': 
'Коллега'}, 'Батя': {'Номер телефона': ['8955441213', '8266565656'], 'Место жительства': 'Рязань', 'Кем приходтся': 'Отец'}}

def save():
    with open("phonebook.json", "w", encoding = "utf -8") as pbk:
        pbk.write(json.dumps(sp, ensure_ascii=False))
    print('Телефонная книга была успешно сохранена в файле phonebook.json')

def load():
    with open("phonebook.json", "r", encoding = "utf -8") as pbk:
        sp = json.load(pbk)
    print('Телефонная книга была успешно загружена')

while True:
    command = input('Введите команду: ')
    if command == '/all':
        print('Вот текущий список контактов: ')
        for k, v in sp.items():
            print(k, v)
    elif command == '/add':
        name = input('Введите имя нового контакта: ')
        if name in sp:
            print('Контакт уже существует!')
        else:
            quantity = int(input('Укажите количство номеров: '))
            phones = []
            for i in range(quantity):
                number = input(f'Введите {i+1} номер: ')
                phones.append(number)
            city = input('Место жительства: ')
            status = input('Кем приходится: ')
            sp[name] = {'Номер телефона': phones, 'Место жительства': city, 'Кем приходится': status}
    if command == '/add.number':
        name = input('Введите имя контакта: ')
        if name not in sp:
            print('Контакта на существует')
        else:
            phone_number = input('Введите номер: ')
            if phone_number in sp[name]['Номер телефона']:
                print('Такой номер телефона уже существует')
            else:
                sp[name]['Номер телефона'].append(phone_number)
    elif command == '/delete':
        name = input('Введите имя контакта, который хотите удалить: ')
        del(sp, name)
        print('Контакт был успешно удален')
    elif command == '/save':
        save()
    elif command == '/load':
        load()
