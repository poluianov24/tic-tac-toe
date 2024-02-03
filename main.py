
def Playground():
    return print(f'''\033[35m {q}\033[35m | {w}\033[35m | {e}\033[35m 
- - - - - -
 {r}\033[35m | {t}\033[35m | {y}\033[35m 
- - - - - -
 {u}\033[35m | {i}\033[35m | {o}\033[35m ''')

def Win():
    if q == w == e == '\033[93mO' or r == t == y == '\033[93mO' or u == i == o == '\033[93mO' or q == r == u == '\033[93mO' or w == t == i == '\033[93mO' or e == y == o == '\033[93mO' or q == t == o == '\033[93mO' or e == t == u == '\033[93mO':
        print('\033[32mПереміг \033[93mOГравець №1\033[32m!!!')
        return 1
    elif q == w == e == '\033[94mX' or r == t == y == '\033[94mX' or u == i == o == '\033[94mX' or q == r == u == '\033[94mX' or w == t == i == '\033[94mX' or e == y == o == '\033[94mX' or q == t == o == '\033[94mX' or e == t == u == '\033[94mX':
        print('\033[32mПереміг \033[94mOГравець №2\033[32m!!!')
        return 2
    elif q != ' ' and w != ' ' and e != ' ' and r != ' ' and t != ' ' and y != ' ' and u != ' ' and i != ' ' and o != ' ':
        print('\033[33mПеремогла дружба!')
        return 3


q = w = e = r = t = y = u = i = o = ' '
win_1 = 0
win_2 = 0
not_win = 0

inp = '\033[32mДля продовження натисніть "Enter" \033[37m(для виходу введіть "0", переглянути № полів - "info")\033[32m: '

res = f'''\033[36m
Рузультати:
\033[93mГравець №1 - {win_1}    \033[94mГравець №2 - {win_2}    \033[36mНічия - {not_win}'''

info = '''\033[32mЗапам'ятайте № полів для здійснення ходів
\033[35m 1 | 2 | 3 
- - - - - -
 4 | 5 | 6 
- - - - - -
 7 | 8 | 9 '''

print(info)
while True:
    while True:
        play1 = input('\033[32mХід гравця \033[93m№1\033[32m. Введіть № поля для ходу \033[37m(для виходу введіть "0", переглянути № полів - "info")\033[32m: ')
        if not play1.isdigit():
            if play1 == 'info':
                print(info)
            else:
                print('\033[91mНекоректно вказано № поля')
        else:
            play1 = int(play1)
            if play1 == 1 and q == ' ':
                q = '\033[93mO'
                break
            elif play1 == 2 and w == ' ':
                w = '\033[93mO'
                break
            elif play1 == 3 and e == ' ':
                e = '\033[93mO'
                break
            elif play1 == 4 and r == ' ':
                r = '\033[93mO'
                break
            elif play1 == 5 and t == ' ':
                t = '\033[93mO'
                break
            elif play1 == 6 and y == ' ':
                y = '\033[93mO'
                break
            elif play1 == 7 and u == ' ':
                u = '\033[93mO'
                break
            elif play1 == 8 and i == ' ':
                i = '\033[93mO'
                break
            elif play1 == 9 and o == ' ':
                o = '\033[93mO'
                break
            elif play1 == 0:
                print(res)
                print('\033[31m\nДо зустрічі!')
                exit()
            elif play1 > 9:
                print('\033[91mДо вибору доступні поля від 1 до 9')
            else:
                print('\033[91mОбране поле зайнято, оберіть пусте поле!')
                pass

    Playground()
    win = Win()
    if win == 1:
        win_1 += 1
        print(res)
        cont = input(f'{inp}')
        if cont == '0':
            print(res)
            print('\033[31m\nДо зустрічі!')
            break
        elif cont == 'info':
            print(info)
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue
    elif win == 2:
        win_2 += 1
        print(res)
        cont = input(f'{inp}')
        if cont == '0':
            print(res)
            print('\033[31m\nДо зустрічі!')
            break
        elif cont == 'info':
            print(info)
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue
    elif win == 3:
        not_win += 1
        print(res)
        cont = input(f'{inp}')
        if cont == '0':
            print(res)
            print('\033[31m\nДо зустрічі!')
            break
        elif cont == 'info':
            print(info)
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue

    while True:
        play2 = input('\033[32mХід гравця \033[94m№2\033[32m. Введіть № поля для ходу \033[37m(для виходу введіть "0", переглянути № полів - "info")\033[32m: ')
        if not play2.isdigit():
            if play2 == 'info':
                print(info)
            else:
                print('\033[91mНекоректно вказано № поля')
        else:
            play2 = int(play2)
            if play2 == 1 and q == ' ':
                q = '\033[94mX'
                break
            elif play2 == 2 and w == ' ':
                w = '\033[94mX'
                break
            elif play2 == 3 and e == ' ':
                e = '\033[94mX'
                break
            elif play2 == 4 and r == ' ':
                r = '\033[94mX'
                break
            elif play2 == 5 and t == ' ':
                t = '\033[94mX'
                break
            elif play2 == 6 and y == ' ':
                y = '\033[94mX'
                break
            elif play2 == 7 and u == ' ':
                u = '\033[94mX'
                break
            elif play2 == 8 and i == ' ':
                i = '\033[94mX'
                break
            elif play2 == 9 and o == ' ':
                o = '\033[94mX'
                break
            elif play2 == 0:
                print(res)
                print('\033[31m\nДо зустрічі!')
                exit()
            elif play2 > 9:
                print('\033[91mДо вибору доступні поля від 1 до 9')
            else:
                print('\033[91mОбране поле зайнято, оберіть пусте поле!')
                pass

    Playground()
    win = Win()
    if win == 1:
        win_1 += 1
        print(res)
        cont = input(f'{inp}')
        if cont == '0':
            print(res)
            print('\033[31m\nДо зустрічі!')
            break
        elif cont == 'info':
            print(info)
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue
    elif win == 2:
        win_2 += 1
        print(res)
        cont = input(f'{inp}')
        if cont == '0':
            print(res)
            print('\033[31m\nДо зустрічі!')
            break
        elif cont == 'info':
            print(info)
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue
    elif win == 3:
        not_win += 1
        print(res)
        cont = input(f'{inp}')
        if cont == '0':
            print(res)
            print('\033[31m\nДо зустрічі!')
            break
        elif cont == 'info':
            print(info)
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue