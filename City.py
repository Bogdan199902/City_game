import random


def read_and_write_txt():  # Запись из файла в список
    data = open('Список городов России.txt', 'r')
    cities = list()
    for i in data:
        i = i[0:-1]
        cities.append(i)
    data.close()
    return cities  # нумерация ключей от 0 до 1120


def all_list_with_city():
    fool_list = read_and_write_txt()
    return fool_list


def first_step_by_comp():  # Первый ход компьютера
    cities = all_list_with_city()
    digit = random.randint(0, len(cities))
    res = cities[digit]
    print('Компьютер:', res)
    data = open('Log_for_game.txt', 'w')
    data.write('Компьютер: ' + res + '\n')
    data.close()
    return res  # компьютер начинает и выдает случайный город из списка


def step_by_computer(all_list, city_point):  # Ход компьютера
    all_city = all_list_with_city()
    stop = -1
    mark = -1
    while stop != 0:
        for i in all_city:
            check_1 = False
            check_2 = False
            if i[0] == city_point[-1].upper():
                check_1 = True
                mark = 0
                if i not in all_list:
                    check_2 = True
            if check_2 and check_1:
                data = open('Log_for_game.txt', 'a')
                data.write('Компьютер: ' + i + '\n')
                data.close()
                return i
        if mark == -1:  # Если не найдено ни одно слово, то ищем по первой букве
            for i in all_city:
                check_1 = False
                check_2 = False
                if i[0] == city_point[0]:
                    check_1 = True
                    if i not in all_list:
                        check_2 = True
                if check_2 and check_1:
                    data = open('Log_for_game.txt', 'a')
                    data.write('Компьютер: ' + i + '\n')
                    data.close()
                    return i
            return 0
        else:
            return 0


def check_for_step(all_list, city_point):  # Проверка на корректность
    count = 0
    while count != 5:
        print('Ваш ход, введите ваш город:')
        inp_city = input()
        count += 1
        check_1 = False
        check_2 = False
        check_3 = False
        if inp_city in all_list_with_city():
            check_1 = True
        if inp_city not in all_list:
            check_2 = True
        if city_point[-1] == inp_city[0].lower():
            check_3 = True
        if check_3 and check_2 and check_1:
            data = open('Log_for_game.txt', 'a')
            data.write('Пользователь: ' + inp_city + '\n')
            data.close()
            return inp_city
        else:
            print('Ошибка, повторите попытку, попыток осталось:', 5-count)
    return 0


def game():
    flag = 0
    stop = 0
    city = first_step_by_comp()
    pre_city = list()
    while stop != -1:  # Одна итерация - один ход
        if flag % 2 == 0 and flag != 0:  # Ход комп
            city = step_by_computer(pre_city, city)
            if city == 0:
                return 'Компьютер побежден'
            print('Компьютер:', city)
        if flag % 2 == 1:  # Ход пользователя
            city = check_for_step(pre_city, city)
            if city == 0:
                return 'Вы проиграли'
            print('Пользователь:', city)
        flag += 1
        pre_city.append(city)


print('Это не игра в кальмара, это игра в города', 'Готовы показать компьютеру, что вы лучше? (да, нет)', sep='\n')
n = input()
if n == 'да':
    print(game())
if n == 'нет':
    print('Ну ладно, было приятно пообщаться')
