
def Playground():
    return print(f'''\033[35m {q} | {w} | {e} 
- - - - - -
 {r} | {t} | {y} 
- - - - - -
 {u} | {i} | {o} ''')

def Win():
    if q == w == e == 'O' or r == t == y == 'O' or u == i == o == 'O' or q == r == u == 'O' or w == t == i == 'O' or e == y == o == 'O' or q == t == o == 'O' or e == t == u == 'O':
        print('\033[32mПереміг гравець 1!')
        return 1
    elif q == w == e == 'X' or r == t == y == 'X' or u == i == o == 'X' or q == r == u == 'X' or w == t == i == 'X' or e == y == o == 'X' or q == t == o == 'X' or e == t == u == 'X':
        print('\033[32mПереміг гравець 2!')
        return 2
    elif q != ' ' and w != ' ' and e != ' ' and r != ' ' and t != ' ' and y != ' ' and u != ' ' and i != ' ' and o != ' ':
        print('\033[32mПеремогла дружба!')
        return 3


q = w = e = r = t = y = u = i = o = ' '
win_1 = 0
win_2 = 0
not_win = 0
print('''\033[32mЗапам'ятайте № полів для здійснення ходів
\033[35m 1 | 2 | 3 
- - - - - -
 4 | 5 | 6 
- - - - - -
 7 | 8 | 9 ''')

while True:
    while True:
        play1 = input('\033[33mХід гравця 1. Введіть № поля для ходу \033[34m(для виходу введіть "0")\033[33m: ')
        if not play1.isdigit():
            continue
        else:
            play1 = int(play1)
            if play1 == 1 and q == ' ':
                q = 'O'
                break
            elif play1 == 2 and w == ' ':
                w = 'O'
                break
            elif play1 == 3 and e == ' ':
                e = 'O'
                break
            elif play1 == 4 and r == ' ':
                r = 'O'
                break
            elif play1 == 5 and t == ' ':
                t = 'O'
                break
            elif play1 == 6 and y == ' ':
                y = 'O'
                break
            elif play1 == 7 and u == ' ':
                u = 'O'
                break
            elif play1 == 8 and i == ' ':
                i = 'O'
                break
            elif play1 == 9 and o == ' ':
                o = 'O'
                break
            elif play1 == 0:
                exit()
            else:
                print('\033[31mОбране поле зайнято, оберіть пусте поле!')
                pass

    Playground()
    win = Win()
    if win == 1:
        win_1 += 1
        print(f'\033[36mГравець №1 - {win_1}    Гравець №2 - {win_2}    Нічия - {not_win}')
        cont = input('\033[33mДля продовження натисніть "Enter" \033[34m(для виходу введіть "0")\033[33m: ')
        if cont == '0':
            break
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue
    elif win == 2:
        win_2 += 1
        print(f'\033[36mГравець №1 - {win_1}    Гравець №2 - {win_2}    Нічия - {not_win}')
        cont = input('\033[33mДля продовження натисніть "Enter" \033[34m(для виходу введіть "0")\033[33m: ')
        if cont == '0':
            break
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue
    elif win == 3:
        not_win += 1
        print(f'\033[36mГравець №1 - {win_1}    Гравець №2 - {win_2}    Нічия - {not_win}')
        cont = input('\033[33mДля продовження натисніть "Enter" \033[34m(для виходу введіть "0")\033[33m: ')
        if cont == '0':
            break
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue

    while True:
        play2 = input('\033[33mХід гравця 2. Введіть № поля для ходу \033[34m(для виходу введіть "0")\033[33m: ')
        if not play2.isdigit():
            continue
        else:
            play2 = int(play2)
            if play2 == 1 and q == ' ':
                q = 'X'
                break
            elif play2 == 2 and w == ' ':
                w = 'X'
                break
            elif play2 == 3 and e == ' ':
                e = 'X'
                break
            elif play2 == 4 and r == ' ':
                r = 'X'
                break
            elif play2 == 5 and t == ' ':
                t = 'X'
                break
            elif play2 == 6 and y == ' ':
                y = 'X'
                break
            elif play2 == 7 and u == ' ':
                u = 'X'
                break
            elif play2 == 8 and i == ' ':
                i = 'X'
                break
            elif play2 == 9 and o == ' ':
                o = 'X'
                break
            elif play2 == 0:
                exit()
            else:
                print('\033[31mОбране поле зайнято, оберіть пусте поле!')
                pass

    Playground()
    win = Win()
    if win == 1:
        win_1 += 1
        print(f'\033[36mГравець №1 - {win_1}    Гравець №2 - {win_2}    Нічия - {not_win}')
        cont = input('\033[33mДля продовження натисніть "Enter" \033[34m(для виходу введіть "0")\033[33m: ')
        if cont == '0':
            break
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue
    elif win == 2:
        win_2 += 1
        print(f'\033[36mГравець №1 - {win_1}    Гравець №2 - {win_2}    Нічия - {not_win}')
        cont = input('\033[33mДля продовження натисніть "Enter" \033[34m(для виходу введіть "0")\033[33m: ')
        if cont == '0':
            break
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue
    elif win == 3:
        not_win += 1
        print(f'\033[36mГравець №1 - {win_1}    Гравець №2 - {win_2}    Нічия - {not_win}')
        cont = input('\033[33mДля продовження натисніть "Enter" \033[34m(для виходу введіть "0")\033[33m: ')
        if cont == '0':
            break
        else:
            q = w = e = r = t = y = u = i = o = ' '
            continue