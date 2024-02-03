
def Playground():
    return print(f''' {q} | {w} | {e} 
- - - - - -
 {r} | {t} | {y} 
- - - - - -
 {u} | {i} | {o} ''')


q = w = e = r = t = y = u = i = o = ' '
win_1 = 0
win_2 = 0
print(''' 1 | 2 | 3 
- - - - - -
 4 | 5 | 6 
- - - - - -
 7 | 8 | 9 ''')

while True:
    while True:
        play1 = int(input('Хід гравця 1. Введіть № поля для ходу: '))
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
        else:
            print('Обране поле зайнято, оберіть пусте поле!')
            pass
    Playground()

    if q == w == e == 'O' or r == t == y == 'O' or u == i == o == 'O' or q == r == u == 'O' or w == t == i == 'O' or e == y == o == 'O' or q == t == o == 'O' or e == t == u == 'O':
        print('Переміг гравець 1!')
        win_1 += 1
        print(f'Гравець №1 - {win_1}   Гравець №2 - {win_2}')
        cont = input('Для продовження введіть "r", для виходу введіть "e": ')
        if cont == 'r':
            q = w = e = r = t = y = u = i = o = ' '
            continue
        elif cont == 'e':
            break
    elif q == w == e == 'X' or r == t == y == 'X' or u == i == o == 'X' or q == r == u == 'X' or w == t == i == 'X' or e == y == o == 'X' or q == t == o == 'X' or e == t == u == 'X':
        print('Переміг гравець 2!')
        win_2 += 1
        print(f'Гравець №1 - {win_1}   Гравець №2 - {win_2}')
        cont = input('Для продовження введіть "r", для виходу введіть "e": ')
        if cont == 'r':
            q = w = e = r = t = y = u = i = o = ' '
            continue
        elif cont == 'e':
            break

    while True:
        play2 = int(input('Хід гравця 2. Введіть № поля для ходу: '))
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
        else:
            print('Обране поле зайнято, оберіть пусте поле!')
            pass
    Playground()

    if q == w == e == 'O' or r == t == y == 'O' or u == i == o == 'O' or q == r == u == 'O' or w == t == i == 'O' or e == y == o == 'O' or q == t == o == 'O' or e == t == u == 'O':
        print('Переміг гравець 1!')
        win_1 += 1
        print(f'Гравець №1 - {win_1}   Гравець №2 - {win_2}')
        cont = input('Для продовження введіть "r", для виходу введіть "e": ')
        if cont == 'r':
            q = w = e = r = t = y = u = i = o = ' '
            continue
        elif cont == 'e':
            break
    elif q == w == e == 'X' or r == t == y == 'X' or u == i == o == 'X' or q == r == u == 'X' or w == t == i == 'X' or e == y == o == 'X' or q == t == o == 'X' or e == t == u == 'X':
        print('Переміг гравець 2!')
        win_2 += 1
        print(f'Гравець №1 - {win_1}   Гравець №2 - {win_2}')
        cont = input('Для продовження введіть "r", для виходу введіть "e": ')
        if cont == 'r':
            q = w = e = r = t = y = u = i = o = ' '
            continue
        elif cont == 'e':
            break