a=input('Игра:\n')
while a != 'game':
    print('Введите слово game\n')
    a=input('Игра:')
if a =='game':
    print('Угадай число')
    for i in range(3):
        b = input('Введите число от 1 до 10\n')
while b !='5':
    print('Игра окончена')
if b =='5':
    print('Вы выйграли билет на концерт Егора Крида')
elif b =='off':
        print('До свидания')